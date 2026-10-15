#!/usr/bin/env bash
# Capture a pinned, real runner execution. Does not claim independent verification.
set -uo pipefail
umask 077

readonly REPO_URL="https://github.com/Evank253/Global-Intelligence.git"
readonly RUNNER_COMMIT="9a3d6768b0338203b478afe883ea13c46d7a7578"
readonly BASELINE_COMMIT="754fb1ff22da0de58ec4db525f137d09a06ae75a"
readonly SPEC_COMMIT="0fdb465382a0104ed7ae9870b0a5df4325575fbf"
readonly RUNNER_BLOB="bacacb4252911486c252bd87e34a4976b75eb4db"
readonly SANDBOX_LABEL="harness-validity observation — not a certified baseline value"
readonly SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
readonly REPO_ROOT="$(git -C "$SCRIPT_DIR/.." rev-parse --show-toplevel 2>/dev/null || cd "$SCRIPT_DIR/.." && pwd)"
readonly VALIDATOR="$REPO_ROOT/tools/validate_federation_evidence.py"

if ! command -v git >/dev/null 2>&1; then echo "BLOCKED: git is required" >&2; exit 20; fi
if ! command -v python3 >/dev/null 2>&1; then echo "BLOCKED: python3 is required" >&2; exit 20; fi
if ! command -v sha256sum >/dev/null 2>&1; then echo "BLOCKED: sha256sum is required" >&2; exit 20; fi
if [[ ! -f "$VALIDATOR" ]]; then echo "BLOCKED: validator missing: $VALIDATOR" >&2; exit 20; fi

# Unique output directory; never delete or reuse an existing evidence directory.
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
EVIDENCE_ROOT="${EVIDENCE_ROOT:-$REPO_ROOT/evidence/runs}"
OUT="$EVIDENCE_ROOT/$STAMP"
mkdir -p -- "$EVIDENCE_ROOT" || exit 20
if ! mkdir -- "$OUT"; then echo "BLOCKED: evidence directory already exists: $OUT" >&2; exit 20; fi
OUT="$(cd -- "$OUT" && pwd)"
WORK="$(mktemp -d "${TMPDIR:-/tmp}/federation-runner.XXXXXXXX")" || exit 20
cleanup() { rm -rf -- "$WORK"; }
trap cleanup EXIT

{
  printf 'run_started_utc=%s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
  printf 'runner_commit=%s\n' "$RUNNER_COMMIT"
  printf 'baseline_commit=%s\n' "$BASELINE_COMMIT"
  printf 'spec_commit=%s\n' "$SPEC_COMMIT"
  printf 'sandbox_label=%s\n' "$SANDBOX_LABEL"
  printf 'host=%s\n' "$(uname -a)"
  printf 'python_version=%s\n' "$(python3 --version 2>&1)"
  printf 'git_version=%s\n' "$(git --version)"
} > "$OUT/environment.txt"

# Fetch the exact runner commit; do not run from the moving audit branch.
if ! git clone --quiet --no-checkout "$REPO_URL" "$WORK/repo" >"$OUT/git-clone.stdout.log" 2>"$OUT/git-clone.stderr.log"; then
  printf 'BLOCKED: clone failed; inspect git-clone.stderr.log\n' >&2
  printf '20\n' > "$OUT/runner.exit-code.txt"
  exit 20
fi
if ! git -C "$WORK/repo" fetch --quiet --no-tags origin "$RUNNER_COMMIT" >"$OUT/git-fetch.stdout.log" 2>"$OUT/git-fetch.stderr.log"; then
  printf 'BLOCKED: pinned runner fetch failed\n' >&2
  printf '20\n' > "$OUT/runner.exit-code.txt"
  exit 20
fi
if ! git -C "$WORK/repo" checkout --quiet --detach "$RUNNER_COMMIT"; then
  printf 'BLOCKED: pinned runner checkout failed\n' >&2
  printf '20\n' > "$OUT/runner.exit-code.txt"
  exit 20
fi

ACTUAL_HEAD="$(git -C "$WORK/repo" rev-parse HEAD)"
ACTUAL_RUNNER_BLOB="$(git -C "$WORK/repo" rev-parse "$RUNNER_COMMIT:tools/federation_baseline_runner.py")"
if [[ "$ACTUAL_HEAD" != "$RUNNER_COMMIT" || "$ACTUAL_RUNNER_BLOB" != "$RUNNER_BLOB" ]]; then
  printf 'BLOCKED: runner identity mismatch; head=%s blob=%s\n' "$ACTUAL_HEAD" "$ACTUAL_RUNNER_BLOB" >&2
  printf '20\n' > "$OUT/runner.exit-code.txt"
  exit 20
fi

# Confirm all pinned implementation source objects at the declared baseline commit.
declare -A SOURCE_PINS=(
  ["kcn_v6/federation_layer/federation_manager.py"]="d78b9fc67db006aa458a2d12649bbf0392c4636e"
  ["kcn_v6/federation_layer/trust_handshake.py"]="c882dcfaa780b722bd24e8cf1538c20f1c71e8b7"
  ["kcn_v6/federation_layer/sync_protocol.py"]="14e84ac22c3f438bb8f829b69512e8ffede2ea3f"
  ["kcn_v6/federation_layer/node_registry.py"]="e9f0d1d047fa29b0a65ebe217609d1de22767063"
  ["kcn_v6/federation_layer/__init__.py"]="256132d2e420c38cbf7bc9c6e63448579cfaaa29"
)
: > "$OUT/source-pin-checks.txt"
for path in "${!SOURCE_PINS[@]}"; do
  expected="${SOURCE_PINS[$path]}"
  actual="$(git -C "$WORK/repo" rev-parse "$BASELINE_COMMIT:$path" 2>/dev/null || true)"
  printf '%s expected=%s actual=%s\n' "$path" "$expected" "$actual" >> "$OUT/source-pin-checks.txt"
  if [[ "$actual" != "$expected" ]]; then
    printf 'BLOCKED: source blob mismatch at %s\n' "$path" >&2
    printf '20\n' > "$OUT/runner.exit-code.txt"
    exit 20
  fi
done

# Run the real pinned runner and preserve stdout, stderr, and its exact exit status.
set +e
(
  cd "$WORK/repo" &&
  python3 tools/federation_baseline_runner.py --output-dir "$OUT"
) >"$OUT/runner.stdout.log" 2>"$OUT/runner.stderr.log"
RUNNER_RC=$?
set -e
printf '%s\n' "$RUNNER_RC" > "$OUT/runner.exit-code.txt"

python3 - "$OUT/capture-metadata.json" "$RUNNER_COMMIT" "$BASELINE_COMMIT" "$SPEC_COMMIT" "$SANDBOX_LABEL" "$ACTUAL_HEAD" "$ACTUAL_RUNNER_BLOB" "$RUNNER_RC" <<'PY'
import json, os, sys
path, runner, baseline, spec, label, head, blob, rc = sys.argv[1:]
payload = {
    "capture_type": "PINNED_RUNNER_CAPTURE_001",
    "runner_commit": runner,
    "baseline_commit": baseline,
    "spec_commit": spec,
    "sandbox_label": label,
    "runner_checkout_head": head,
    "runner_script_blob": blob,
    "runner_exit_code": int(rc),
    "independent_verification": "NOT_MEASURED",
    "baseline_qualification": "NOT_MEASURED",
}
with open(path, "x", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, sort_keys=True)
    f.write("\n")
PY

# Hash every captured file except the inventory itself; use relative paths.
(
  cd "$OUT" &&
  find . -type f ! -name inventory.sha256 -print0 |
    sort -z |
    xargs -0 -r sha256sum
) > "$OUT/inventory.sha256"

if [[ "$RUNNER_RC" -ne 0 ]]; then
  echo "BLOCKED: runner exit=$RUNNER_RC; raw capture retained at $OUT" >&2
  exit "$RUNNER_RC"
fi

set +e
python3 "$VALIDATOR" "$OUT" >"$OUT/validator.stdout.log" 2>"$OUT/validator.stderr.log"
VALIDATOR_RC=$?
set -e
# Add validator outputs to the inventory, now that validation has completed.
(
  cd "$OUT" &&
  find . -type f ! -name inventory.sha256 -print0 |
    sort -z |
    xargs -0 -r sha256sum
) > "$OUT/inventory.sha256"

if [[ "$VALIDATOR_RC" -ne 0 ]]; then
  echo "EVIDENCE_VALIDATION_FAILED: raw capture retained at $OUT" >&2
  exit "$VALIDATOR_RC"
fi

echo "CAPTURE_VALIDATED: $OUT"
echo "Interpretation boundary: harness-validity observation only; not a certified baseline or independent audit."

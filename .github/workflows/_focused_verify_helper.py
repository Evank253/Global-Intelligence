#!/usr/bin/env python3
"""
Controlled evidence-package builder + validator runner for the temporary
oidc-federation-focused-verify workflow.

This script:
  - Builds a synthetic evidence package that satisfies the structural /
    pin requirements of the patched validate_federation_evidence.py.
  - Records that the package is synthetic.
  - Invokes the actual patched validator.
  - Writes exit codes and logs so the workflow can upload them.

It never fabricates a real federation execution or claims qualification.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

# Pins must match the patched validator on the focused branch
RUNNER_COMMIT = "9a3d6768b0338203b478afe883ea13c46d7a7578"
BASELINE_COMMIT = "754fb1ff22da0de58ec4db525f137d09a06ae75a"
SPEC_COMMIT = "0fdb465382a0104ed7ae9870b0a5df4325575fbf"
MATRIX_BLOB = "5568396eb0e39ab5c927bd80051f701aa3bd3aeb"
SOURCE_BLOBS = {
    "kcn_v6/federation_layer/federation_manager.py": "d78b9fc67db006aa458a2d12649bbf0392c4636e",
    "kcn_v6/federation_layer/trust_handshake.py": "c882dcfaa780b722bd24e8cf1538c20f1c71e8b7",
    "kcn_v6/federation_layer/sync_protocol.py": "14e84ac22c3f438bb8f829b69512e8ffede2ea3f",
    "kcn_v6/federation_layer/node_registry.py": "e9f0d1d047fa29b0a65ebe217609d1de22767063",
    "kcn_v6/federation_layer/__init__.py": "256132d2e420c38cbf7bc9c6e63448579cfaaa29",
}
EXPECTED_IDS = (
    [f"T-AUTH-{i:03}" for i in range(1, 8)]
    + [f"T-AGREE-{i:03}" for i in range(1, 6)]
    + [f"T-EVID-{i:03}" for i in range(1, 5)]
    + [f"T-LEDGER-{i:03}" for i in range(1, 5)]
    + [f"T-EXEC-{i:03}" for i in range(1, 3)]
    + [f"T-INV-{i:02}" for i in range(1, 11)]
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def make_report() -> dict:
    basis = {
        "basis_id": "ENVIRONMENT-CLASS-BASIS-001",
        "detection_rule": "sandbox_local_observation",
        "detected_class": "sandbox_smoke_test",
        "oidc_verified": False,
        "cryptographic_attestation": False,
    }
    results = [
        {
            "test_id": tid,
            "status": "NOT_MEASURED",
            "execution_mode": "SOURCE_INSPECTION",
            "reason": "synthetic fixture for focused-branch validator check only",
            "invocations": [],
            "test_execution_adequacy": "SUFFICIENT_FOR_OBSERVATION",
        }
        for tid in EXPECTED_IDS
    ]
    counts = {s: sum(1 for r in results if r["status"] == s)
              for s in ("PASS", "FAIL", "NOT_MEASURED", "BLOCKED")}
    mode_counts = {
        m: sum(1 for r in results if r["execution_mode"] == m)
        for m in ("BEHAVIORAL_EXECUTION", "SOURCE_INSPECTION",
                  "TABLE_DERIVATION", "BLOCKED")
    }
    return {
        "artifact_type": "MANIFEX-MILLENNIUM-FEDERATION-BASELINE-REPORT-001",
        "status": "OBSERVATION_ONLY_NOT_INDEPENDENT_VERIFICATION",
        "run_id": "focused-verify-synthetic-0001",
        "environment_class": "sandbox_smoke_test",
        "environment_class_basis": basis,
        "independent_verification": "NOT_MEASURED",
        "baseline_qualification": "NOT_MEASURED",
        "baseline": {
            "pinned_commit_sha": BASELINE_COMMIT,
            "executed_checkout_head_sha": RUNNER_COMMIT,
            "pinned_commit_is_ancestor_of_head": True,
            "source_file_blob_checks": {
                p: {"expected_blob_sha": s, "actual_blob_sha": s, "status": "PASS"}
                for p, s in SOURCE_BLOBS.items()
            },
        },
        "specification": {
            "commit_sha": SPEC_COMMIT,
            "matrix_git_blob_sha": MATRIX_BLOB,
            "matrix_tests_loaded": 32,
        },
        "results": results,
        "counts": counts,
        "execution_mode_counts": mode_counts,
    }


def make_metadata() -> dict:
    return {
        "runner_commit": RUNNER_COMMIT,
        "baseline_commit": BASELINE_COMMIT,
        "environment_class": "sandbox_smoke_test",
        "environment_class_basis": {
            "basis_id": "ENVIRONMENT-CLASS-BASIS-001",
            "detection_rule": "sandbox_local_observation",
            "detected_class": "sandbox_smoke_test",
            "oidc_verified": False,
            "cryptographic_attestation": False,
        },
        "observation_label": "harness-validity observation — not a certified baseline value",
        "fixture_status": "SYNTHETIC — not a real federation execution",
    }


def build_package(pkg: Path) -> None:
    if pkg.exists():
        for child in pkg.iterdir():
            if child.is_file():
                child.unlink()
    pkg.mkdir(parents=True, exist_ok=True)

    write(pkg / "federation-baseline-synthetic.json",
          json.dumps(make_report(), indent=2) + "\n")
    write(pkg / "federation-baseline-synthetic.md",
          "# Synthetic fixture\n\nNot a real federation execution.\n")
    write(pkg / "runner.stdout.log", "synthetic runner stdout\n")
    write(pkg / "runner.stderr.log", "synthetic runner stderr\n")
    write(pkg / "runner.exit-code.txt", "0\n")
    write(pkg / "capture-metadata.json",
          json.dumps(make_metadata(), indent=2) + "\n")
    write(pkg / "validator.stdout.log", "validator started (synthetic)\n")
    write(pkg / "validator.stderr.log", "")

    files = [
        "federation-baseline-synthetic.json",
        "federation-baseline-synthetic.md",
        "runner.stdout.log",
        "runner.stderr.log",
        "runner.exit-code.txt",
        "capture-metadata.json",
        "validator.stdout.log",
        "validator.stderr.log",
    ]
    lines = [f"{sha256_file(pkg / n)}  {n}" for n in files]
    write(pkg / "inventory.sha256", "\n".join(lines) + "\n")

    # Explicit marker so reviewers cannot mistake this for real evidence
    write(pkg / "FIXTURE_STATUS.txt",
          "SYNTHETIC\nThis package was generated by _focused_verify_helper.py "
          "for focused-branch validator testing only.\n"
          "It does not represent a real federation baseline execution.\n"
          "Federation qualification and independent verification remain NOT_MEASURED.\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--results-dir", type=Path, required=True)
    parser.add_argument(
        "--validator-path",
        type=Path,
        default=Path("tools/validate_federation_evidence.py"),
        help="Path to the exact validator binary under test (from isolated checkout)",
    )
    args = parser.parse_args()

    pkg = args.output_dir / "controlled-package"
    build_package(pkg)
    print(f"Built synthetic package at {pkg}")
    print("FIXTURE_STATUS=SYNTHETIC")

    validator = args.validator_path
    if not validator.is_file():
        print(f"ERROR: validator not found at {validator}", file=sys.stderr)
        return 1
    print(f"Using validator binary: {validator.resolve()}")

    proc = subprocess.run(
        [sys.executable, str(validator), str(pkg)],
        capture_output=True,
        text=True,
        timeout=60,
    )
    write(args.output_dir / "validator.stdout.log", proc.stdout)
    write(args.output_dir / "validator.stderr.log", proc.stderr)
    write(args.output_dir / "validator.exit-code.txt", f"{proc.returncode}\n")

    result = {
        "fixture_status": "SYNTHETIC",
        "validator_exit_code": proc.returncode,
        "validator_stdout_excerpt": proc.stdout[:1000],
        "validator_stderr_excerpt": proc.stderr[:1000],
        "meaning": (
            "Controlled synthetic package exercised the patched validator. "
            "This is not a real federation execution. "
            "Federation qualification and independent verification remain NOT_MEASURED."
        ),
    }
    args.results_dir.mkdir(parents=True, exist_ok=True)
    write(args.results_dir / "validator_run.json",
          json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())

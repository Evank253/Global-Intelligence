# Federation Dual-Track Audit — Recovery Ledger

**Status:** INITIALIZED — no audit run performed  
**Branch:** `federation-dual-track-audit`  
**Recorded starting commit:** `44bad8099833ab9346d3de168b3694f9c89023ef`  
**Starting point:** verified head of `federation-harness-001` at branch creation  
**Baseline classification:** `NOT_MEASURED`

## Scope and preservation rules

This branch is for additive audit, capture, and evidence-validation artifacts. It does not redefine the frozen federation matrix, change the pinned federation implementation, or modify historical attempt records. In particular, `BLOCKED-001` remains frozen and must not be rewritten.

The branch name is a location, not evidence of successful verification. Every run must record its actual checked-out commit and all input pins. A successful launcher exit or valid JSON document is not evidence that the federation passed its requirements.

## Verified source identity pins

- Runner branch: `federation-baseline-runner-001`
- Runner commit: `9a3d6768b0338203b478afe883ea13c46d7a7578`
- Federation baseline commit: `754fb1ff22da0de58ec4db525f137d09a06ae75a`
- Frozen specification commit: `0fdb465382a0104ed7ae9870b0a5df4325575fbf`
- Frozen matrix Git blob: `5568396eb0e39ab5c927bd80051f701aa3bd3aeb`

The five pinned federation source blob IDs were previously compared with the files at the pinned federation commit and matched. The specification commit and matrix blob still require an explicit independent re-check before execution. A pin written in a file is not itself proof that the corresponding object was retrieved and verified.

## Branch existence and provenance

The exact audit branch was absent before creation. It was created from the explicit commit SHA `44bad8099833ab9346d3de168b3694f9c89023ef`, not from an inferred branch name. The branch creation did not run the federation runner and did not produce baseline evidence.

## Required execution contract

1. Resolve the branch and record the actual starting/checkout SHA.
2. Verify the runner commit and expected runner file.
3. Verify the federation baseline commit.
4. Independently compare all five pinned source Git blob IDs.
5. Verify the frozen specification commit and exact matrix blob ID.
6. Stop on any identity mismatch; do not silently substitute a nearby revision.
7. If preflight succeeds, execute the pinned runner and preserve its exit code, stdout, stderr, environment, and raw output files.
8. Validate the resulting package and have a reviewer independent of the runner author inspect raw evidence.

## Status vocabulary

- `PASS`: evidence supports the stated test criterion.
- `FAIL`: captured observation contradicts the stated criterion; scope the claim to that observation.
- `NOT_MEASURED`: no adequate measurement supports a conclusion.
- `BLOCKED`: execution or evidence production could not validly proceed.

These statuses are not interchangeable. In particular, missing interfaces or runner failures must not be converted into product failures or passes.

## Current state

- Audit branch: **created**
- Initial commit SHA: **recorded**
- Corrected launcher and package validator: **not yet committed at ledger creation**
- Frozen spec/matrix independent re-check: **pending**
- Qualifying baseline run: **NOT_MEASURED**
- Evidence-schema validation against a real run: **NOT PERFORMED**
- Independent audit: **NOT PERFORMED**
- Human ratification: **NOT PERFORMED**

Update this ledger additively as work occurs. Do not backdate events or change earlier attempt classifications to make later work appear earlier.


## Preflight check record — frozen specification and matrix

**Check date:** 2026-10-14 (current session; GitHub commit metadata reports the specification commit was created 2026-10-14 UTC)  
**Method:** Retrieve the exact commit by SHA from the declared repository, then retrieve each target file using that exact commit SHA as the ref. Compare the returned Git object IDs with the recorded pins.  
**Scope:** Object identity only. This is not the independent implementation/evidence audit.

| Check | Expected | Retrieved | Result |
|---|---|---|---|
| Specification repository commit | `0fdb465382a0104ed7ae9870b0a5df4325575fbf` | `0fdb465382a0104ed7ae9870b0a5df4325575fbf` | MATCH |
| Matrix path at pinned commit | `MANIFEX-MILLENNIUM-FEDERATION-TEST-MATRIX-001.md` | Retrieved at the exact pinned commit | MATCH |
| Matrix Git blob SHA | `5568396eb0e39ab5c927bd80051f701aa3bd3aeb` | `5568396eb0e39ab5c927bd80051f701aa3bd3aeb` | MATCH |
| Specification file at pinned commit | `MANIFEX-MILLENNIUM-FEDERATION-VERIFICATION-SPECIFICATION-001.md` | Retrieved at the exact pinned commit; blob `a1d16c557b447c60ea40575f94d202721800b781` | Retrieved; no prior spec-file blob pin was declared for comparison |

References:
- Specification commit: https://github.com/Evank253/Manifex-millennium-/commit/0fdb465382a0104ed7ae9870b0a5df4325575fbf
- Matrix at pinned commit: https://github.com/Evank253/Manifex-millennium-/blob/0fdb465382a0104ed7ae9870b0a5df4325575fbf/MANIFEX-MILLENNIUM-FEDERATION-TEST-MATRIX-001.md
- Specification at pinned commit: https://github.com/Evank253/Manifex-millennium-/blob/0fdb465382a0104ed7ae9870b0a5df4325575fbf/MANIFEX-MILLENNIUM-FEDERATION-VERIFICATION-SPECIFICATION-001.md

**Outcome:** The specified commit exists at the expected SHA, and the matrix file's retrieved Git blob SHA matches the expected pin. This preflight check did not detect a mismatch in either of the two requested pins. No federation tests were run as part of this check. This retrieval verifies GitHub object identity; it is not a substitute for an independently controlled reviewer or execution environment.



## Environment-class gate implementation

The audit branch now defines and enforces the required `report.json.environment_class` field with exactly three allowed values: `sandbox_smoke_test`, `github_hosted_ci`, and `controlled_host`. The retired `sandbox_validity_label` is rejected in the report rather than coexisting with the new field.

- `sandbox_smoke_test` and `github_hosted_ci` require both `independent_verification` and `baseline_qualification` to remain `NOT_MEASURED`.
- Report and capture metadata must agree on `environment_class`.
- `controlled_host` requires a pre-run decision-record reference with a non-empty decision ID, SHA-256 digest, `auditor_accepted: true`, and `accepted_before_run: true`.
- The current capture launcher explicitly blocks `controlled_host`; that path is not authorized until decision-record handling and controlled-host operation are implemented and reviewed. This prevents an ordinary CI capture from claiming controlled-host status.
- The pinned runner source is not modified. `tools/annotate_environment_class.py` adds capture-side environment metadata after the runner writes its raw report and marks that annotation as capture-side.
- The GitHub Actions workflow explicitly sets `github_hosted_ci`.

Specification: `docs/evidence-environment-class-addendum-001.md`.

**Validation boundary:** The validator and capture artifacts have been updated in GitHub, but no local syntax/test run or real runner execution is claimed by this ledger entry. Until the workflow output and raw artifacts are inspected, evidence-schema validation against real output remains `NOT_PERFORMED`, independent audit remains `NOT_PERFORMED`, and baseline qualification remains `NOT_MEASURED`.


## CI environment-label integrity correction

**Recorded after diagnosis of stale CI failures and substrate misclassification risk.**

The capture path now defaults the declared environment class to `sandbox_smoke_test`. It derives the expected class from runtime signals: `GITHUB_ACTIONS=true`, non-empty `RUNNER_OS`, and non-empty `GITHUB_RUN_ID` are required to classify a run as `github_hosted_ci`; otherwise the detected class is `sandbox_smoke_test`. A mismatch between the declared and detected class blocks capture. The annotator independently repeats this consistency check before modifying the report. The `controlled_host` path remains blocked.

The workflow push path filter now includes `tools/annotate_environment_class.py`, so changing this hard dependency triggers capture validation.

Commits:
- Capture substrate derivation: `4cb612ec218dd4d7a52783b295a05d07cc4ab594`
- Annotator runtime-signal corroboration: `0bfcaa7a90b8d5a0c2b247a0da639c984cf4a541`
- Workflow path-filter correction: `a5f2e14525e1df394c916f2d6ca0c1ff4eca7d2d`

**Validation boundary:** GitHub file contents were re-fetched after these writes and the relevant code/path-filter markers were confirmed. No new CI run, local test run, or new real runner execution is claimed by this entry. Runtime environment variables are corroboration signals, not cryptographic attestation against a deliberately hostile process that can forge its own environment; independent substrate verification remains required. Existing mislabeled captures must not be reclassified retroactively as genuine CI evidence merely because their report says `github_hosted_ci`. The latest CI-tested commit remains the one established by the previously supplied diagnosis until a new Actions run exercises the updated branch tip.


## Environment-class basis-field wiring

The capture metadata writer now persists `environment_class_basis` alongside `environment_class`, using the same basis identifier, detection rule, GitHub Actions signals, detected class, and explicit `cryptographic_attestation: false` value that the annotator writes into the runner report. The validator requires the report and capture-metadata basis objects to match exactly. This closes the data-flow gap between defining the basis, recording it, and validating it.

Commit: `811bc56b01e2a3275dcc4a72f4ce6e9acfeef0bb`.

**Important:** this is signal recording and consistency enforcement, not OIDC attestation. GitHub Actions environment variables remain forgeable by a process that controls its environment. OIDC-backed identity/attestation is not implemented here. No new CI result or local test result is claimed; the latest commit needs to be exercised by the workflow before the change can be marked validated.

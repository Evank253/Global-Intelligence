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

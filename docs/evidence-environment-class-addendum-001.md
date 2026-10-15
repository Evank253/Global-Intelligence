# Evidence Package Schema — Environment Class Addendum 001

**Status:** Normative validator contract; no measurement result claimed.

## Required report field

The `report.json` field `environment_class` is required and accepts exactly these values:

- `sandbox_smoke_test` — constrained ephemeral sandbox (2 vCPU, approximately 2 GB, no KVM); harness-validity observations only.
- `github_hosted_ci` — GitHub-hosted Actions runner; harness-validity observations only, not the designated controlled host.
- `controlled_host` — the only class eligible to produce a certified baseline value. Before the run, the auditor must explicitly accept the machine definition in a decision record.

`environment_class` replaces `sandbox_validity_label`; they must not coexist. The validator rejects reports that omit `environment_class`, use an unknown value, or include the retired `sandbox_validity_label` field. The capture metadata and report must carry the same class.

## Non-controlled environment gates

For `sandbox_smoke_test` and `github_hosted_ci`, both `independent_verification` and `baseline_qualification` must equal `NOT_MEASURED`. These environments can establish harness validity only; neither can act as its own independent audit or produce a certified baseline value.

## Controlled host acceptance gate

For `controlled_host`, the report must include `environment.controlled_host_decision_record` with all of:

- `decision_id`: non-empty identifier for the decision record.
- `decision_record_sha256`: lowercase 64-character SHA-256 digest of that record.
- `auditor_accepted`: `true`.
- `accepted_before_run`: `true`.

This records an explicit, pre-run acceptance claim. The digest and booleans are not self-authenticating: the independent auditor must retrieve the referenced decision record, verify its digest and timestamp/provenance, and confirm the accepting auditor had the appropriate role. If the record cannot be independently confirmed, the controlled-host gate is not satisfied.

## Promotion ladder

1. `sandbox_smoke_test`: proves only that the harness can move in the constrained sandbox.
2. `github_hosted_ci`: proves only that the harness can move on the GitHub-hosted CI substrate.
3. `controlled_host`: potentially eligible for a certified baseline only after its pre-run machine-definition decision record is accepted and the measurement evidence passes review.
4. Independent audit: a separate process on a different substrate inspects raw evidence the runner did not produce. Certification remains blocked until this independent gate and the project's ratification process are complete.

A valid JSON report, successful process exit, matching status counts, or `controlled_host` label alone is not certification. Frozen source pins, raw outputs, capture metadata, and per-test adequacy remain separate requirements.

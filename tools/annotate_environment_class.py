#!/usr/bin/env python3
"""Annotate a pinned runner report with capture-side substrate classification."""

import json
import os
import sys
from pathlib import Path

ALLOWED = {"sandbox_smoke_test", "github_hosted_ci", "controlled_host"}

def main() -> int:
    if len(sys.argv) != 3:
        print("usage: annotate_environment_class.py EVIDENCE_DIR ENVIRONMENT_CLASS", file=sys.stderr)
        return 2
    root = Path(sys.argv[1])
    environment_class = sys.argv[2]
    if environment_class not in ALLOWED:
        print(f"invalid environment_class: {environment_class}", file=sys.stderr)
        return 2
    if environment_class == "controlled_host":
        print("controlled_host requires an accepted decision record; annotation tool does not authorize it", file=sys.stderr)
        return 2
    # Independently corroborate the caller's declaration against runtime signals.
    is_github_actions = (
        os.environ.get("GITHUB_ACTIONS") == "true"
        and bool(os.environ.get("RUNNER_OS"))
        and bool(os.environ.get("GITHUB_RUN_ID"))
    )
    detected = "github_hosted_ci" if is_github_actions else "sandbox_smoke_test"
    if environment_class != detected:
        print(
            f"environment_class mismatch: declared={environment_class}, detected={detected}; "
            "GITHUB_ACTIONS=true, RUNNER_OS, and GITHUB_RUN_ID are required for github_hosted_ci",
            file=sys.stderr,
        )
        return 2
    reports = sorted(root.glob("federation-baseline-*.json"))
    if len(reports) != 1:
        print(f"expected exactly one runner report; found {len(reports)}", file=sys.stderr)
        return 2
    path = reports[0]
    report = json.loads(path.read_text(encoding="utf-8"))
    report["environment_class"] = environment_class
    report["baseline_qualification"] = "NOT_MEASURED"
    # Preserve the verified OIDC identity basis for CI; local sandbox signals
    # remain explicitly non-cryptographic.
    basis_file = os.environ.get("MANIFEX_OIDC_BASIS_FILE")
    if environment_class == "github_hosted_ci":
        if not basis_file:
            print("verified OIDC basis file is required for github_hosted_ci", file=sys.stderr)
            return 2
        try:
            basis = json.loads(Path(basis_file).read_text(encoding="utf-8"))
        except Exception:
            print("OIDC basis file is unreadable or invalid", file=sys.stderr)
            return 2
        if basis.get("basis_id") != "ENVIRONMENT-CLASS-BASIS-002" or basis.get("oidc_verified") is not True:
            print("OIDC basis is not verified", file=sys.stderr)
            return 2
        if basis.get("run_id") != os.environ.get("GITHUB_RUN_ID") or basis.get("sha") != os.environ.get("GITHUB_SHA"):
            print("OIDC basis does not match this workflow run", file=sys.stderr)
            return 2
        report["environment_class_basis"] = basis
    else:
        report["environment_class_basis"] = {
            "basis_id": "ENVIRONMENT-CLASS-BASIS-001",
            "detection_rule": "github_actions_true_and_runner_os_and_run_id_present",
            "github_actions": os.environ.get("GITHUB_ACTIONS") == "true",
            "runner_os": os.environ.get("RUNNER_OS") or None,
            "github_run_id": os.environ.get("GITHUB_RUN_ID") or None,
            "github_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT") or None,
            "detected_class": detected,
            "cryptographic_attestation": False,
        }
    report["capture_annotation"] = {
        "field_added_by": "tools/annotate_environment_class.py",
        "pinned_runner_modified": False,
        "independent_verification": "NOT_MEASURED",
    }
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

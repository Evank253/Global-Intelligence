#!/usr/bin/env python3
"""Annotate a pinned runner report with capture-side substrate classification."""

import json
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
    reports = sorted(root.glob("federation-baseline-*.json"))
    if len(reports) != 1:
        print(f"expected exactly one runner report; found {len(reports)}", file=sys.stderr)
        return 2
    path = reports[0]
    report = json.loads(path.read_text(encoding="utf-8"))
    report["environment_class"] = environment_class
    report["baseline_qualification"] = "NOT_MEASURED"
    report["capture_annotation"] = {
        "field_added_by": "tools/annotate_environment_class.py",
        "pinned_runner_modified": False,
        "independent_verification": "NOT_MEASURED",
    }
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())

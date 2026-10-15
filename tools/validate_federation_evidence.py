#!/usr/bin/env python3
"""Validate a captured federation baseline report without interpreting it as certification."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

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
STATUSES = {"PASS", "FAIL", "NOT_MEASURED", "BLOCKED"}
MODES = {"BEHAVIORAL_EXECUTION", "SOURCE_INSPECTION", "TABLE_DERIVATION", "BLOCKED"}
EXPECTED_IDS = (
    [f"T-AUTH-{i:03}" for i in range(1, 8)]
    + [f"T-AGREE-{i:03}" for i in range(1, 6)]
    + [f"T-EVID-{i:03}" for i in range(1, 5)]
    + [f"T-LEDGER-{i:03}" for i in range(1, 5)]
    + [f"T-EXEC-{i:03}" for i in range(1, 3)]
    + [f"T-INV-{i:02}" for i in range(1, 11)]
)


class ValidationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence_dir", type=Path)
    args = parser.parse_args()
    root = args.evidence_dir.resolve()
    require(root.is_dir(), f"evidence directory does not exist: {root}")

    json_reports = sorted(root.glob("federation-baseline-*.json"))
    md_reports = sorted(root.glob("federation-baseline-*.md"))
    require(len(json_reports) == 1, f"expected exactly one runner JSON report; found {len(json_reports)}")
    require(len(md_reports) == 1, f"expected exactly one runner Markdown report; found {len(md_reports)}")
    required_capture = [
        "runner.stdout.log", "runner.stderr.log", "runner.exit-code.txt",
        "capture-metadata.json", "inventory.sha256",
    ]
    for name in required_capture:
        require((root / name).is_file(), f"required capture artifact missing: {name}")

    exit_text = (root / "runner.exit-code.txt").read_text(encoding="utf-8").strip()
    require(exit_text == "0", f"runner exit code is not zero: {exit_text!r}")
    metadata = json.loads((root / "capture-metadata.json").read_text(encoding="utf-8"))
    require(metadata.get("runner_commit") == RUNNER_COMMIT, "capture metadata runner commit mismatch")
    require(metadata.get("baseline_commit") == BASELINE_COMMIT, "capture metadata baseline commit mismatch")
    require(metadata.get("sandbox_label") == "harness-validity observation — not a certified baseline value",
            "sandbox label missing or altered")

    report = json.loads(json_reports[0].read_text(encoding="utf-8"))
    require(report.get("artifact_type") == "MANIFEX-MILLENNIUM-FEDERATION-BASELINE-REPORT-001",
            "unexpected report artifact_type")
    require(report.get("status") == "OBSERVATION_ONLY_NOT_INDEPENDENT_VERIFICATION",
            "report status missing or unexpected")
    require(report.get("independent_verification") == "NOT_MEASURED",
            "independent_verification must remain NOT_MEASURED")
    baseline = report.get("baseline", {})
    require(baseline.get("pinned_commit_sha") == BASELINE_COMMIT, "baseline commit pin mismatch in report")
    require(baseline.get("executed_checkout_head_sha") == RUNNER_COMMIT,
            "executed checkout HEAD does not equal pinned runner commit")
    require(baseline.get("pinned_commit_is_ancestor_of_head") is True,
            "pinned baseline is not reported as an ancestor of the checkout")
    source_checks = baseline.get("source_file_blob_checks", {})
    for path, expected in SOURCE_BLOBS.items():
        entry = source_checks.get(path, {})
        require(entry.get("expected_blob_sha") == expected, f"missing or incorrect expected blob pin: {path}")
        require(entry.get("actual_blob_sha") == expected, f"source blob mismatch: {path}")
        require(entry.get("status") == "PASS", f"source blob check not PASS: {path}")

    spec = report.get("specification", {})
    require(spec.get("commit_sha") == SPEC_COMMIT, "specification commit pin mismatch in report")
    require(spec.get("matrix_git_blob_sha") == MATRIX_BLOB, "matrix blob pin mismatch in report")
    require(spec.get("matrix_tests_loaded") == 32, "runner did not load exactly 32 frozen matrix tests")

    results = report.get("results")
    require(isinstance(results, list) and len(results) == 32, "report must contain exactly 32 result rows")
    ids = [row.get("test_id") for row in results]
    require(len(set(ids)) == len(ids), "duplicate test IDs in report")
    require(set(ids) == set(EXPECTED_IDS), "report test IDs do not match the frozen Track A ID set")
    for row in results:
        require(row.get("status") in STATUSES, f"invalid status for {row.get('test_id')}")
        require(row.get("execution_mode") in MODES, f"invalid execution mode for {row.get('test_id')}")
        require(isinstance(row.get("reason"), str) and row["reason"].strip(),
                f"missing rationale/reason for {row.get('test_id')}")
        require(isinstance(row.get("invocations"), list), f"invocations is not a list for {row.get('test_id')}")
        if row.get("test_execution_adequacy") == "INSUFFICIENT_FOR_REQUIREMENT":
            require(row.get("status") != "PASS",
                    f"row {row.get('test_id')} claims PASS despite insufficient requirement coverage")

    expected_counts = {status: sum(1 for row in results if row["status"] == status) for status in STATUSES}
    require(report.get("counts") == expected_counts, "top-level status counts do not match result rows")
    expected_modes = {mode: sum(1 for row in results if row["execution_mode"] == mode)
                      for mode in ("BEHAVIORAL_EXECUTION", "SOURCE_INSPECTION", "TABLE_DERIVATION", "BLOCKED")}
    require(report.get("execution_mode_counts") == expected_modes,
            "top-level execution-mode counts do not match result rows")

    inventory_lines = (root / "inventory.sha256").read_text(encoding="utf-8").splitlines()
    require(bool(inventory_lines), "inventory.sha256 is empty")
    for line in inventory_lines:
        require(re.fullmatch(r"[0-9a-f]{64}  .+", line) is not None,
                f"malformed inventory line: {line!r}")
    inventory_names = {line.split("  ", 1)[1] for line in inventory_lines}
    for name in [json_reports[0].name, md_reports[0].name, *required_capture[:-1]]:
        require(name in inventory_names, f"artifact missing from hash inventory: {name}")

    print(json.dumps({
        "validation": "PASS",
        "meaning": "capture package structure and pin consistency validated; not federation qualification",
        "run_id": report.get("run_id"),
        "track_a_rows": len(results),
        "status_counts": expected_counts,
        "execution_mode_counts": expected_modes,
        "independent_verification": "NOT_MEASURED",
        "baseline_qualification": "NOT_MEASURED",
    }, indent=2))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"EVIDENCE_VALIDATION_FAILED: {exc}", file=sys.stderr)
        raise SystemExit(2)

#!/usr/bin/env python3
"""
MANIFEX-MILLENNIUM-FEDERATION-BASELINE-RUNNER-001\n\nWorkflow trigger revision: baseline runner is executed in GitHub Actions.

Read-only baseline probes against the real KCN v6 federation classes.
This runner does not implement a substitute federation and does not certify
itself or the target implementation.

Pinned inputs:
  Global-Intelligence commit: 754fb1ff22da0de58ec4db525f137d09a06ae75a
  MANIFEX-MILLENNIUM-FEDERATION-TEST-MATRIX-001 commit:
    0fdb465382a0104ed7ae9870b0a5df4325575fbf

Run from a checkout of Global-Intelligence:
  python tools/federation_baseline_runner.py --matrix /path/to/MANIFEX-MILLENNIUM-FEDERATION-TEST-MATRIX-001.md

The matrix may also be downloaded from the pinned public commit if --matrix
is omitted. Outputs are evidence artifacts, not independent verification.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib
import inspect
import json
import os
import platform
import re
import subprocess
import sys
import traceback
import urllib.request
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

BASELINE_REPO = "Evank253/Global-Intelligence"
BASELINE_COMMIT = "754fb1ff22da0de58ec4db525f137d09a06ae75a"
SPEC_REPO = "Evank253/Manifex-millennium-"
SPEC_COMMIT = "0fdb465382a0104ed7ae9870b0a5df4325575fbf"
MATRIX_PATH = "MANIFEX-MILLENNIUM-FEDERATION-TEST-MATRIX-001.md"
MATRIX_BLOB_SHA = "5568396eb0e39ab5c927bd80051f701aa3bd3aeb"

# Git blob IDs pin the exact source files tested, even when this runner is
# committed on a child branch whose HEAD is newer than BASELINE_COMMIT.
PINNED_SOURCE_BLOBS = {
    "kcn_v6/federation_layer/federation_manager.py": "d78b9fc67db006aa458a2d12649bbf0392c4636e",
    "kcn_v6/federation_layer/trust_handshake.py": "c882dcfaa780b722bd24e8cf1538c20f1c71e8b7",
    "kcn_v6/federation_layer/sync_protocol.py": "14e84ac22c3f438bb8f829b69512e8ffede2ea3f",
    "kcn_v6/federation_layer/node_registry.py": "e9f0d1d047fa29b0a65ebe217609d1de22767063",
    "kcn_v6/federation_layer/__init__.py": "256132d2e420c38cbf7bc9c6e63448579cfaaa29",
}

VALID_STATUSES = {"PASS", "FAIL", "NOT_MEASURED", "BLOCKED"}
TABLE_ROW_RE = re.compile(r"^\|\s*(T-[^|]+)\|(.+)$")


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


def git_output(root: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(root), *args],
        text=True,
        capture_output=True,
        check=True,
    )
    return proc.stdout.strip()


def locate_repo_root(start: Path) -> Path:
    try:
        return Path(git_output(start, "rev-parse", "--show-toplevel")).resolve()
    except Exception as exc:
        raise RuntimeError(f"Runner must execute inside a Git checkout: {exc}") from exc


def load_matrix(matrix_path: Path | None) -> tuple[bytes, str]:
    if matrix_path is not None:
        data = matrix_path.read_bytes()
    else:
        url = (
            f"https://raw.githubusercontent.com/{SPEC_REPO}/"
            f"{SPEC_COMMIT}/{MATRIX_PATH}"
        )
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "MANIFEX-MILLENNIUM-Federation-Baseline-Runner/001"},
        )
        with urllib.request.urlopen(request, timeout=15) as response:
            data = response.read()

    actual_blob = git_blob_sha(data)
    if actual_blob != MATRIX_BLOB_SHA:
        raise ValueError(
            "Frozen matrix integrity check failed: "
            f"expected Git blob {MATRIX_BLOB_SHA}, got {actual_blob}"
        )
    return data, actual_blob


def parse_matrix(data: bytes) -> list[dict[str, str]]:
    text = data.decode("utf-8")
    rows: list[dict[str, str]] = []
    for line in text.splitlines():
        match = TABLE_ROW_RE.match(line)
        if not match:
            continue
        test_id = match.group(1).strip()
        if not re.fullmatch(r"T-[A-Z]+-\d{3}|T-INV-\d{2}", test_id):
            continue
        fields = [part.strip() for part in match.group(2).strip().strip("|").split("|")]
        if len(fields) != 7:
            raise ValueError(f"Unexpected matrix row shape for {test_id}: {len(fields)} fields")
        rows.append({
            "test_id": test_id,
            "requirement_id": fields[0],
            "protocol": fields[1],
            "setup": fields[2],
            "adversarial_injection": fields[3],
            "expected_outcome": fields[4],
            "evidence_artifact": fields[5],
            "matrix_status": fields[6],
        })
    ids = [row["test_id"] for row in rows]
    if len(rows) != 32:
        raise ValueError(f"Expected 32 matrix tests; found {len(rows)}")
    if len(set(ids)) != len(ids):
        raise ValueError("Frozen matrix contains duplicate test IDs")
    return rows


def verify_source_blobs(root: Path) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for relative, expected in PINNED_SOURCE_BLOBS.items():
        path = root / relative
        if not path.is_file():
            result[relative] = {"status": "BLOCKED", "reason": "source file missing"}
            continue
        actual = git_blob_sha(path.read_bytes())
        result[relative] = {
            "expected_blob_sha": expected,
            "actual_blob_sha": actual,
            "status": "PASS" if actual == expected else "FAIL",
        }
    return result


def api_surface(classes: list[type]) -> dict[str, list[str]]:
    surface: dict[str, list[str]] = {}
    for cls in classes:
        methods = []
        for name, member in inspect.getmembers(cls, predicate=callable):
            if name.startswith("_"):
                continue
            try:
                methods.append(f"{name}{inspect.signature(member)}")
            except (TypeError, ValueError):
                methods.append(name)
        surface[f"{cls.__module__}.{cls.__name__}"] = methods
    return surface


def result_record(
    test: dict[str, str],
    status: str,
    reason: str,
    request: Any = None,
    response: Any = None,
    observed: Any = None,
) -> dict[str, Any]:
    if status not in VALID_STATUSES:
        raise ValueError(f"Invalid status {status}")
    return {
        **test,
        "status": status,
        "reason": reason,
        "request": request,
        "response": response,
        "observed": observed,
    }


def run_supported_probe(test: dict[str, str], classes: dict[str, type]) -> dict[str, Any] | None:
    test_id = test["test_id"]

    # AUTH-001: the real handshake currently ignores signature content.
    if test_id == "T-AUTH-001":
        request = {"peer_node_id": "baseline-probe", "signature": ""}
        response = classes["TrustHandshake"]().authenticate_peer(**request)
        status = "FAIL" if response.get("authenticated") is True else "PASS"
        return result_record(
            test, status,
            "Empty signature was accepted as authenticated." if status == "FAIL"
            else "Empty signature was not accepted as authenticated.",
            request, response,
            {"assertion": "authenticated must not be true for an empty signature"},
        )

    # AUTH-007: the pinned API exposes no nonce, message ID, replay cache, or
    # authorization-context parameter. An empty-signature probe would test
    # authentication again, not replay resistance, so this case is NOT_MEASURED.
    if test_id == "T-AUTH-007":
        return result_record(
            test, "NOT_MEASURED",
            "The pinned handshake API exposes no nonce, message ID, replay cache, or authorization context; "
            "replaying a previously accepted authorization cannot be exercised faithfully through this API.",
            {"api": "TrustHandshake.authenticate_peer(peer_node_id, signature)"},
            None,
            {"available_api": api_surface([classes["TrustHandshake"]])},
        )

    # AGREE-003: empty membership still receives a success/consensus response.
    if test_id == "T-AGREE-003":
        request = {"active_nodes": []}
        response = classes["FederationManager"]().sync_federation(**request)
        declares_finality = (
            response.get("network_consensus") == "UNIFIED_GLOBAL_STATE"
            or response.get("sync_status") == "SUCCESS"
        )
        status = "FAIL" if declares_finality else "PASS"
        return result_record(
            test, status,
            "The manager reports consensus/success with zero participants and no vote or quorum input."
            if status == "FAIL" else "No success/finality claim observed for empty membership.",
            request, response,
            {"assertion": "no final decision without valid votes meeting the declared quorum"},
        )

    # EVID-003: registration assigns a verification label without verification evidence.
    if test_id == "T-EVID-003":
        request = {"node_id": "unverified-probe", "capabilities": ["baseline-test"]}
        response = classes["NodeRegistry"]().register(**request)
        status = "FAIL" if response.get("status") == "verified" else "PASS"
        return result_record(
            test, status,
            "Node registration assigns status='verified' without accepting or checking a verification record."
            if status == "FAIL" else "Registration did not assign verified status without evidence.",
            request, response,
            {"assertion": "caller-controlled metadata or bare registration must not establish verification"},
        )

    # INV-03 asks whether a valid signature can be kept distinct from claim truth.
    # The baseline has no cryptographic verifier or claim/evidence-status interface,
    # so an honest status is NOT_MEASURED rather than an invented PASS/FAIL.
    if test_id == "T-INV-03":
        request = {"probe": "inspect signature and claim-verification interfaces"}
        return result_record(
            test, "NOT_MEASURED",
            "The real baseline exposes no cryptographic signature-verification or claim-verification API; "
            "the invariant cannot be behaviorally evaluated through these classes.",
            request, None,
            {"available_api": api_surface(list(classes.values()))},
        )

    return None


def run_test(test: dict[str, str], classes: dict[str, type]) -> dict[str, Any]:
    started = utc_now()
    try:
        supported = run_supported_probe(test, classes)
        if supported is None:
            record = result_record(
                test,
                "NOT_MEASURED",
                "The frozen matrix case has no corresponding callable control in the pinned baseline API. "
                "No mock or substitute protocol was introduced; the available real-class API was inspected.",
                request={
                    "required_scenario": test["adversarial_injection"],
                    "target_api": api_surface(list(classes.values())),
                },
                response=None,
                observed={"execution": "interface inspection only", "behavioral_test_executed": False},
            )
        else:
            record = supported
        record["started_at"] = started
        record["finished_at"] = utc_now()
        record["harness_exception"] = None
        return record
    except Exception as exc:
        # Harness or unexpected adapter exception is BLOCKED, not a product FAIL.
        return result_record(
            test, "BLOCKED",
            "Harness/adapter exception prevented a valid determination; this is not counted as a product failure.",
            request={"test_id": test["test_id"]},
            response=None,
            observed={"exception_type": type(exc).__name__, "exception": str(exc)},
        ) | {
            "started_at": started,
            "finished_at": utc_now(),
            "harness_exception": traceback.format_exc(),
        }


def load_real_classes(root: Path) -> dict[str, type]:
    root_string = str(root)
    if root_string not in sys.path:
        sys.path.insert(0, root_string)
    package = importlib.import_module("kcn_v6.federation_layer")
    return {
        "FederationManager": package.FederationManager,
        "TrustHandshake": package.TrustHandshake,
        "SyncProtocol": package.SyncProtocol,
        "NodeRegistry": package.NodeRegistry,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--matrix", type=Path, help="Local copy of the frozen test matrix Markdown file")
    parser.add_argument("--output-dir", type=Path, default=Path("federation-baseline-evidence"))
    parser.add_argument("--allow-source-mismatch", action="store_true",
                        help="Run despite pinned source-file mismatch; results will be marked BLOCKED.")
    args = parser.parse_args()

    started = utc_now()
    run_id = str(uuid.uuid4())
    try:
        root = locate_repo_root(Path.cwd())
        matrix_bytes, matrix_blob = load_matrix(args.matrix)
        tests = parse_matrix(matrix_bytes)
        source_checks = verify_source_blobs(root)
        mismatches = [p for p, v in source_checks.items() if v.get("status") != "PASS"]

        if mismatches and not args.allow_source_mismatch:
            raise RuntimeError(
                "Pinned baseline source files do not match expected blob IDs: "
                + ", ".join(mismatches)
                + ". Refusing to test a different implementation. Use --allow-source-mismatch "
                  "only for diagnostic work; such results will be BLOCKED."
            )

        if mismatches:
            records = [
                result_record(
                    test, "BLOCKED",
                    "Pinned source integrity mismatch; execution against the declared baseline was not performed.",
                    request={"expected_baseline_commit": BASELINE_COMMIT},
                    response=None,
                    observed={"source_mismatches": mismatches},
                ) | {"started_at": started, "finished_at": utc_now(), "harness_exception": None}
                for test in tests
            ]
            classes = {}
        else:
            classes = load_real_classes(root)
            records = [run_test(test, classes) for test in tests]

        head = git_output(root, "rev-parse", "HEAD")
        branch = git_output(root, "branch", "--show-current")
        try:
            is_ancestor = subprocess.run(
                ["git", "-C", str(root), "merge-base", "--is-ancestor", BASELINE_COMMIT, "HEAD"],
                capture_output=True,
            ).returncode == 0
        except Exception:
            is_ancestor = False

        counts = {status: sum(1 for r in records if r["status"] == status) for status in sorted(VALID_STATUSES)}
        report = {
            "artifact_type": "MANIFEX-MILLENNIUM-FEDERATION-BASELINE-REPORT-001",
            "status": "OBSERVATION_ONLY_NOT_INDEPENDENT_VERIFICATION",
            "run_id": run_id,
            "started_at": started,
            "finished_at": utc_now(),
            "baseline": {
                "repository": BASELINE_REPO,
                "pinned_commit_sha": BASELINE_COMMIT,
                "executed_checkout_head_sha": head,
                "branch": branch,
                "pinned_commit_is_ancestor_of_head": is_ancestor,
                "source_file_blob_checks": source_checks,
            },
            "specification": {
                "repository": SPEC_REPO,
                "commit_sha": SPEC_COMMIT,
                "matrix_path": MATRIX_PATH,
                "matrix_git_blob_sha": matrix_blob,
                "matrix_tests_loaded": len(tests),
            },
            "environment": {
                "python_version": sys.version,
                "implementation": platform.python_implementation(),
                "platform": platform.platform(),
                "os_name": os.name,
                "cwd": str(Path.cwd()),
                "repo_root": str(root),
            },
            "independent_verification": "NOT_MEASURED",
            "counts": counts,
            "results": records,
            "limitations": [
                "This runner is an author-controlled baseline probe, not independent verification.",
                "NOT_MEASURED means the pinned classes expose no adequate behavioral interface for that test.",
                "A FAIL is limited to the explicit observed assertion and does not establish universal insecurity.",
                "No test is PASS merely because the target reports success.",
                "No mock or replacement federation is used.",
            ],
        }

        args.output_dir.mkdir(parents=True, exist_ok=True)
        json_path = args.output_dir / f"federation-baseline-{run_id}.json"
        md_path = args.output_dir / f"federation-baseline-{run_id}.md"
        json_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        lines = [
            "# MANIFEX-MILLENNIUM-FEDERATION-BASELINE-REPORT-001",
            "",
            f"- Run ID: `{run_id}`",
            f"- Started: {started}",
            f"- Finished: {report['finished_at']}",
            f"- Stub repository: `{BASELINE_REPO}`",
            f"- Pinned stub commit: `{BASELINE_COMMIT}`",
            f"- Executed checkout HEAD: `{head}`",
            f"- Specification repository: `{SPEC_REPO}`",
            f"- Specification commit: `{SPEC_COMMIT}`",
            f"- Matrix Git blob SHA: `{matrix_blob}`",
            f"- Tests loaded: {len(tests)}",
            f"- Independent verification: **NOT_MEASURED**",
            "",
            "## Status counts",
            "",
            "| Status | Count |",
            "|---|---:|",
        ]
        for status in ("PASS", "FAIL", "NOT_MEASURED", "BLOCKED"):
            lines.append(f"| {status} | {counts[status]} |")
        lines += ["", "## Per-test observations", ""]
        for item in records:
            lines += [
                f"### {item['test_id']} — {item['status']}",
                f"- Requirement: `{item['requirement_id']}`",
                f"- Reason: {item['reason']}",
                f"- Evidence artifact: `{item['test_id']}` entry in the JSON report",
                "",
            ]
        lines += [
            "## Limitations",
            "",
            "- This report records observations from this run only.",
            "- A harness exception is BLOCKED, never counted as a product FAIL.",
            "- Tests without a corresponding baseline API remain NOT_MEASURED.",
            "- This report is not independent verification or human ratification.",
            "",
        ]
        md_path.write_text("\n".join(lines), encoding="utf-8")

        print(json.dumps({
            "run_id": run_id,
            "counts": counts,
            "json_report": str(json_path),
            "markdown_report": str(md_path),
            "independent_verification": "NOT_MEASURED",
        }, indent=2))
        return 0
    except Exception as exc:
        # A top-level runner failure is a harness block, not a federation FAIL.
        print(json.dumps({
            "run_id": run_id,
            "status": "BLOCKED",
            "started_at": started,
            "finished_at": utc_now(),
            "exception_type": type(exc).__name__,
            "exception": str(exc),
            "traceback": traceback.format_exc(),
            "meaning": "Harness could not produce a valid baseline result; no product FAIL is inferred.",
        }, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

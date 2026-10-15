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
    *,
    execution_mode: str = "SOURCE_INSPECTION",
    invocations: list[dict[str, Any]] | None = None,
    test_execution_adequacy: str = "INSUFFICIENT_FOR_REQUIREMENT",
) -> dict[str, Any]:
    if status not in VALID_STATUSES:
        raise ValueError(f"Invalid status {status}")
    if execution_mode not in {
        "BEHAVIORAL_EXECUTION", "SOURCE_INSPECTION", "TABLE_DERIVATION", "BLOCKED"
    }:
        raise ValueError(f"Invalid execution mode {execution_mode}")
    return {
        **test,
        "status": status,
        "reason": reason,
        "request": request,
        "response": response,
        "observed": observed,
        "execution_mode": execution_mode,
        "test_execution_adequacy": test_execution_adequacy,
        "invocations": invocations or [],
    }


def _invoke(
    instance: Any,
    method_name: str,
    kwargs: dict[str, Any],
) -> dict[str, Any]:
    """Invoke a real pinned-baseline method and retain the raw observation."""
    method = getattr(instance, method_name)
    started = utc_now()
    record: dict[str, Any] = {
        "execution_mode": "BEHAVIORAL_EXECUTION",
        "class": f"{type(instance).__module__}.{type(instance).__name__}",
        "method": method_name,
        "signature": str(inspect.signature(method)),
        "input_kwargs": kwargs,
        "started_at": started,
    }
    try:
        raw = method(**kwargs)
        record.update({
            "outcome": "RETURN",
            "raw_return_type": type(raw).__name__,
            "raw_return": raw,
        })
    except Exception as exc:
        record.update({
            "outcome": "RAISE",
            "exception_type": type(exc).__name__,
            "exception_message": str(exc),
        })
    record["finished_at"] = utc_now()
    return record


def _unsupported(
    test: dict[str, str],
    classes: dict[str, type],
    reason: str,
    invocations: list[dict[str, Any]] | None = None,
    observed: Any = None,
) -> dict[str, Any]:
    return result_record(
        test, "NOT_MEASURED", reason,
        request={"required_scenario": test["adversarial_injection"]},
        response=(invocations[-1].get("raw_return") if invocations and invocations[-1].get("outcome") == "RETURN" else None),
        observed={
            "available_api": api_surface(list(classes.values())),
            "behavioral_invocation_is_not_equivalent_to_requirement_coverage": True,
            **(observed or {}),
        },
        execution_mode="BEHAVIORAL_EXECUTION" if invocations else "SOURCE_INSPECTION",
        invocations=invocations or [],
        test_execution_adequacy="INSUFFICIENT_FOR_REQUIREMENT",
    )


def run_supported_probe(test: dict[str, str], classes: dict[str, type]) -> dict[str, Any] | None:
    """Run actual baseline methods where possible; never turn an unrelated call into test coverage."""
    test_id = test["test_id"]
    invocations: list[dict[str, Any]] = []
    handshake = classes["TrustHandshake"]
    manager = classes["FederationManager"]
    registry = classes["NodeRegistry"]
    sync = classes["SyncProtocol"]

    # Authentication probes. The public method has only peer_node_id/signature;
    # caller authority flags, approval records, scope, and crypto material are absent.
    if test_id in {"T-AUTH-001", "T-AUTH-004", "T-AUTH-005", "T-AUTH-006", "T-AUTH-007", "T-INV-01", "T-INV-03", "T-INV-09"}:
        if test_id == "T-AUTH-001":
            # First preserve what happens when the exact matrix payload is attempted.
            invocations.append(_invoke(handshake(), "authenticate_peer", {
                "peer_node_id": "baseline-probe",
                "signature": "garbage",
                "human_approved": True,
                "verified": True,
                "qualified": True,
            }))
            # Then exercise the accepted public interface with an invalid signature.
            invocations.append(_invoke(handshake(), "authenticate_peer", {
                "peer_node_id": "baseline-probe", "signature": ""
            }))
            last = invocations[-1]
            if last.get("raw_return", {}).get("authenticated") is True:
                status, reason = "FAIL", (
                    "The exact matrix payload is not accepted by the method signature, but the real public "
                    "method then reports authenticated=true for an empty signature. This is an observed "
                    "unsupported authentication claim; flag-handling itself remains unmeasured."
                )
                adequacy = "PARTIAL_DIRECT_OBSERVATION"
            else:
                status, reason, adequacy = "NOT_MEASURED", (
                    "The method did not accept the matrix's authority/status fields; application-level "
                    "refusal semantics and an approval-record path are not exposed."
                ), "INSUFFICIENT_FOR_REQUIREMENT"
            return result_record(test, status, reason, invocations=invocations,
                request={"matrix_payload": {"peer_node_id":"baseline-probe","signature":"garbage","human_approved":True,"verified":True,"qualified":True}},
                response=last.get("raw_return"), observed={"method_invocations": invocations},
                execution_mode="BEHAVIORAL_EXECUTION", test_execution_adequacy=adequacy)
        signature = {
            "T-AUTH-004": "arbitrary-signature",
            "T-AUTH-005": "signature-value-A",
            "T-AUTH-006": "signature-for-P1-presented-as-P2",
            "T-AUTH-007": "replay-byte-identical",
            "T-INV-01": "garbage",
            "T-INV-03": "valid-signature-over-false-claim",
            "T-INV-09": "authorization-without-scope",
        }[test_id]
        peer = "supreme-human-authority" if test_id == "T-INV-01" else (
            "P2" if test_id == "T-AUTH-006" else "baseline-probe"
        )
        first = _invoke(handshake(), "authenticate_peer", {"peer_node_id": peer, "signature": signature})
        invocations.append(first)
        if test_id == "T-AUTH-007":
            invocations.append(_invoke(handshake(), "authenticate_peer", {"peer_node_id": peer, "signature": signature}))
            both_return_authenticated = all(x.get("raw_return", {}).get("authenticated") is True for x in invocations)
            return result_record(test, "FAIL" if both_return_authenticated else "NOT_MEASURED",
                "Byte-identical replay was accepted identically; the API has no nonce, request ID, or replay context."
                if both_return_authenticated else "Replay behavior could not be established from the observed calls.",
                request={"first": {"peer_node_id":peer,"signature":signature}, "replay": {"peer_node_id":peer,"signature":signature}},
                response=[x.get("raw_return", x.get("exception_message")) for x in invocations],
                observed={"method_invocations": invocations, "replay_context_api": False},
                execution_mode="BEHAVIORAL_EXECUTION",
                test_execution_adequacy="PARTIAL_DIRECT_OBSERVATION" if both_return_authenticated else "INSUFFICIENT_FOR_REQUIREMENT")
        returned = first.get("raw_return", {})
        if returned.get("authenticated") is True and test_id in {"T-AUTH-005", "T-AUTH-006", "T-INV-01"}:
            reason = {
                "T-AUTH-005": "An arbitrary signature value was reported authenticated; no key verification was exercised.",
                "T-AUTH-006": "The API has no proposal/domain parameter and reports the P2 peer authenticated from an arbitrary P1-labeled signature.",
                "T-INV-01": "An authority-like peer identity with a garbage signature was reported authenticated; this is an unsupported authentication claim, not proof of authority creation.",
            }[test_id]
            status, adequacy = "FAIL", "PARTIAL_DIRECT_OBSERVATION"
        elif test_id in {"T-AUTH-004", "T-AUTH-005", "T-AUTH-006", "T-INV-01"}:
            status, reason, adequacy = "NOT_MEASURED", "The target response did not establish the matrix's required authority-boundary behavior.", "INSUFFICIENT_FOR_REQUIREMENT"
        else:
            status, reason, adequacy = "NOT_MEASURED", (
                "A method call was captured, but the API has no cryptographic verifier/claim-status interface "
                "to establish a genuinely valid signature over a false claim or scoped authorization."
            ), "INSUFFICIENT_FOR_REQUIREMENT"
        return result_record(test, status, reason, request={"peer_node_id":peer,"signature":signature},
            response=returned, observed={"method_invocations":invocations,"method_has_no_key_or_scope_parameter":True},
            execution_mode="BEHAVIORAL_EXECUTION", test_execution_adequacy=adequacy)

    # Agreement probes. These calls expose membership-counting and unconditional finality,
    # but do not emulate a vote/quorum API that the baseline does not implement.
    if test_id in {"T-AGREE-001", "T-AGREE-002", "T-AGREE-003", "T-AGREE-004", "T-AGREE-005", "T-INV-02", "T-INV-04"}:
        active = {
            "T-AGREE-001": ["a", "a", "a"],
            "T-AGREE-002": ["participant-X:vote-yes", "participant-X:vote-no"],
            "T-AGREE-003": [],
            "T-AGREE-004": ["unregistered-participant"],
            "T-AGREE-005": ["proposal-digest-A", "proposal-digest-B"],
            "T-INV-02": ["proposal-to-create-human-authority"],
            "T-INV-04": ["unanimous-claim-without-evidence"],
        }[test_id]
        invocation = _invoke(manager(), "sync_federation", {"active_nodes": active})
        invocations.append(invocation)
        output = invocation.get("raw_return", {})
        if test_id == "T-AGREE-001" and output.get("node_count") == 3:
            status, reason, adequacy = "FAIL", "Duplicate participant identifiers inflate node_count to 3; the API does not deduplicate membership.", "PARTIAL_DIRECT_OBSERVATION"
        elif test_id in {"T-AGREE-003", "T-AGREE-004"} and (
            output.get("sync_status") == "SUCCESS" or output.get("network_consensus") == "UNIFIED_GLOBAL_STATE"
        ):
            status = "FAIL"
            reason = "The method reports SUCCESS/UNIFIED_GLOBAL_STATE for an empty or unregistered-only participant set without votes or quorum inputs."
            adequacy = "PARTIAL_DIRECT_OBSERVATION"
        else:
            return _unsupported(test, classes,
                "The real method was invoked, but this row requires signed votes, proposal digests, quorum configuration, or domain evidence that the API does not accept. Its generic success output is retained as an observation, not misrepresented as a direct test of that missing control.",
                invocations, {"participant_input": active, "raw_success_claim": output})
        return result_record(test, status, reason, request={"active_nodes":active}, response=output,
            observed={"method_invocations":invocations,"no_vote_or_quorum_parameters":True},
            execution_mode="BEHAVIORAL_EXECUTION", test_execution_adequacy=adequacy)

    # Evidence registry probes. Registration and discovery are real behavior;
    # independence disclosures and evidence ledgers are not implemented by this API.
    if test_id in {"T-EVID-001", "T-EVID-002", "T-EVID-003", "T-EVID-004", "T-INV-06", "T-INV-07", "T-INV-08", "T-INV-10"}:
        if test_id == "T-EVID-003":
            invocation = _invoke(registry(), "register", {"node_id":"unverified-probe","capabilities":["baseline-test"]})
            invocations.append(invocation)
            output = invocation.get("raw_return", {})
            status = "FAIL" if output.get("status") == "verified" else "NOT_MEASURED"
            return result_record(test, status,
                "Bare registration returns status='verified' without a verification record."
                if status == "FAIL" else "No unsupported verified status was observed.",
                request={"node_id":"unverified-probe","capabilities":["baseline-test"]}, response=output,
                observed={"method_invocations":invocations,"verification_record_supplied":False},
                execution_mode="BEHAVIORAL_EXECUTION",
                test_execution_adequacy="PARTIAL_DIRECT_OBSERVATION" if status == "FAIL" else "INSUFFICIENT_FOR_REQUIREMENT")
        if test_id == "T-EVID-004":
            invocations.append(_invoke(registry(), "register", {"node_id":"overwrite-probe","capabilities":["safe-capability"]}))
            invocations.append(_invoke(registry(), "register", {"node_id":"overwrite-probe","capabilities":["nuclear-launch"]}))
            invocations.append(_invoke(registry(), "discover", {"capability":"nuclear-launch"}))
            first, second, discovered = [x.get("raw_return") for x in invocations]
            overwritten = bool(second and second.get("capabilities") == ["nuclear-launch"] and first != second)
            return result_record(test, "FAIL" if overwritten else "NOT_MEASURED",
                "Re-registering the same node silently replaces its prior capability record; no version/history interface is exposed."
                if overwritten else "The test did not establish a silent overwrite.",
                request={"first_registration":{"node_id":"overwrite-probe","capabilities":["safe-capability"]},
                         "second_registration":{"node_id":"overwrite-probe","capabilities":["nuclear-launch"]}},
                response={"first":first,"second":second,"discover":discovered},
                observed={"method_invocations":invocations,"append_only_history_api":False},
                execution_mode="BEHAVIORAL_EXECUTION",
                test_execution_adequacy="PARTIAL_DIRECT_OBSERVATION" if overwritten else "INSUFFICIENT_FOR_REQUIREMENT")
        if test_id == "T-EVID-002":
            invocations.append(_invoke(registry(), "register", {"node_id":"independence-probe","capabilities":["nuclear-launch"]}))
            invocations.append(_invoke(registry(), "discover", {"capability":"nuclear-launch"}))
        elif test_id == "T-INV-06":
            invocations.append(_invoke(registry(), "register", {"node_id":"status-probe","capabilities":["capability-A"]}))
            invocations.append(_invoke(sync(), "synchronize_delta", {"state_hash":"caller-controlled-hash"}))
        elif test_id == "T-INV-07":
            invocations.append(_invoke(registry(), "register", {"node_id":"unknown-status-probe","capabilities":["NOT_MEASURED"]}))
        elif test_id == "T-INV-08":
            invocations.append(_invoke(registry(), "register", {"node_id":"component-only","capabilities":["component-qualified"]}))
        elif test_id == "T-INV-10":
            invocations.append(_invoke(sync(), "synchronize_delta", {"state_hash":"self-attestation-probe"}))
        else:
            invocations.append(_invoke(manager(), "sync_federation", {"active_nodes":["node-without-evidence"]}))
        return _unsupported(test, classes,
            "Behavioral calls were captured, but the pinned API exposes no evidence sufficiency, independence-disclosure, status-transition, qualification-inheritance, or independent-verification-status control for this requirement.",
            invocations, {"raw_observations": [x.get("raw_return", x.get("exception_message")) for x in invocations]})

    # Synchronization/ledger probes. These execute synchronize_delta, but do not
    # pretend its echoed hash is a ledger, checkpoint, or durable-commit interface.
    if test_id in {"T-LEDGER-001", "T-LEDGER-002", "T-LEDGER-003", "T-LEDGER-004"}:
        hashes = {
            "T-LEDGER-001": "garbage-caller-hash",
            "T-LEDGER-002": "checkpoint-branch-A",
            "T-LEDGER-003": "failure-between-write-and-ack",
            "T-LEDGER-004": "replace-committed-event",
        }
        first = _invoke(sync(), "synchronize_delta", {"state_hash": hashes[test_id]})
        invocations.append(first)
        if test_id == "T-LEDGER-002":
            invocations.append(_invoke(sync(), "synchronize_delta", {"state_hash":"checkpoint-branch-B"}))
        return _unsupported(test, classes,
            "synchronize_delta was behaviorally invoked and its raw IN_SYNC/hash-echo response was captured, but the pinned API has no event ledger, checkpoint, persistence, or recovery interface. This does not count as execution of the ledger requirement.",
            invocations, {"echo_stub_diagnostic":True,
                          "raw_sync_claims":[x.get("raw_return", x.get("exception_message")) for x in invocations],
                          "ledger_requirement_executed":False})

    # Execution protocol does not exist in the pinned API.
    if test_id in {"T-EXEC-001", "T-EXEC-002"}:
        return None

    # Remaining cross-protocol invariants: execute a relevant public method only
    # when doing so adds an observation; never infer an unexposed invariant passed.
    if test_id == "T-INV-05":
        invocations.append(_invoke(sync(), "synchronize_delta", {"state_hash":"rewritten-history-hash"}))
        return _unsupported(test, classes, "The sync method was invoked, but no append-only ledger or independent checkpoint API exists.", invocations,
                            {"ledger_requirement_executed":False})
    return None


def run_test(test: dict[str, str], classes: dict[str, type]) -> dict[str, Any]:
    started = utc_now()
    try:
        supported = run_supported_probe(test, classes)
        if supported is None:
            record = result_record(
                test,
                "NOT_MEASURED",
                "The pinned baseline exposes no callable control adequate to exercise this requirement. "
                "The API surface was inspected; no mock or replacement protocol was introduced.",
                request={"required_scenario": test["adversarial_injection"]},
                response=None,
                observed={"available_api": api_surface(list(classes.values())),
                          "behavioral_test_executed": False},
                execution_mode="SOURCE_INSPECTION",
                test_execution_adequacy="INSUFFICIENT_FOR_REQUIREMENT",
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
            execution_mode="BLOCKED",
            test_execution_adequacy="BLOCKED",
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
            "execution_mode_counts": {mode: sum(1 for r in records if r.get("execution_mode") == mode) for mode in ("BEHAVIORAL_EXECUTION", "SOURCE_INSPECTION", "TABLE_DERIVATION", "BLOCKED")},
            "measurement_system_warnings": [
                "A method invocation is not automatically adequate coverage of the mapped requirement.",
                "PARTIAL_DIRECT_OBSERVATION means the observed behavior supports only part of the test criterion.",
                "Rows with test_execution_adequacy=INSUFFICIENT_FOR_REQUIREMENT remain NOT_MEASURED even if an adjacent method was invoked.",
                "Invocation evidence is captured by this harness but is not independently authenticated by the report; a reviewer must reproduce or independently inspect it.",
            ],
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
            "## Execution mode counts",
            "",
            "| Mode | Count |",
            "|---|---:|",
            *[f"| {mode} | {sum(1 for r in records if r.get('execution_mode') == mode)} |" for mode in ("BEHAVIORAL_EXECUTION", "SOURCE_INSPECTION", "TABLE_DERIVATION", "BLOCKED")],
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
                f"- Execution mode: `{item.get('execution_mode', 'SOURCE_INSPECTION')}`",
                f"- Test execution adequacy: `{item.get('test_execution_adequacy', 'INSUFFICIENT_FOR_REQUIREMENT')}`",
                f"- Captured method invocations: {len(item.get('invocations', []))}",
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

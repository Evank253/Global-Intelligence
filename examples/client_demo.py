#!/usr/bin/env python3
"""
KCN Intelligence OS - SDK Client Demonstration Example
Demonstrates connecting to KCN Intelligence OS, submitting reasoning queries,
and inspecting the 6-Question Accountability Passport and v4 Network metadata.
"""

from kcn_v3.sdk.client import KCNClient


def main():
    print("================================================================================")
    print("      KCN v3/v4 DEVELOPER SDK - CLIENT DEMONSTRATION")
    print("================================================================================")

    # Instantiate client pointing to local server or embedded orchestrator
    client = KCNClient(api_key="kcn_dev_key_alpha_001", host="http://localhost:8000")

    # Check health
    health = client.get_health()
    print(f"[SDK Diagnostics] Status: {health.get('status')} | Version: {health.get('version', 'v4.0')}")

    # Submit multi-agent query
    query_text = "What bio-inspired structural feedback mechanics can harden urban bridges against resonant shear strain?"
    print(f"\n[SDK Query Submission] Asking: '{query_text}'")

    response = client.query(query_text, context={"priority": "HIGH", "domain": "engineering"})

    print("\n[SDK Execution Response Received]")
    print(f"  - Session ID: {response.get('session_id')}")
    print(f"  - Execution Milestone: {response.get('phase_milestone')}")

    verdict = response.get("master_verdict", {})
    print(f"  - Consensus Verdict: {verdict.get('consensus_verdict')}")
    print(f"  - Evidence Strength: {verdict.get('aggregate_evidence_strength')}")
    print(f"  - Black Box Risk Score: {verdict.get('black_box_risk_score')}")

    passport = response.get("accountability_passport", {}).get("audit_trail", {})
    print("\n[6-Question Accountability Passport Audit Trail]")
    for q_key, q_val in passport.items():
      print(f"  {q_key}: {q_val}")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
KCN Intelligence OS - Accountability Audit Exporter Example
Extracts 6-Question Accountability Passports and exports tamper-evident JSON audit packages.
"""

import json
from accountability.permanent_accountability import PermanentAccountabilitySystem
from independent_validation.audit_exporter import AuditExporter


def main():
    print("Generating sample 6-question accountability passport...")
    pas = PermanentAccountabilitySystem()
    passport = pas.generate_audit_passport(
        decision_id="dec_example_urban_resilience_042",
        reason_why="De-centralize water retention pumps to prevent flash flood surges.",
        evidence_sources=["sensor_telemetry_v4", "hydrology_expert_swarm"],
        approved_by="Executive Cortex Safety Gate",
        rejected_alternatives=["Central mega-reservoir expansion"],
        observed_outcome="Peak water flow rate lowered by 34.2% in urban basin.",
        lesson_learned="Distributed micro-barriers outperform localized high-volume dams."
    )

    exporter = AuditExporter()
    audit_pkg = exporter.export_audit_package("session_audit_demo_042", passport)

    print("\n[Cryptographic Audit Package Summary]")
    print(f"Signature: {audit_pkg['sha256_signature']}")
    print(f"Export Format: {audit_pkg['export_format']}")
    print(f"Black Box Risk Score: {passport['black_box_risk_score']}")

    output_path = "/home/user/test_results/sample_export_audit_package.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(audit_pkg, f, indent=2)
    print(f"Exported audit package saved to: {output_path}")


if __name__ == "__main__":
    main()

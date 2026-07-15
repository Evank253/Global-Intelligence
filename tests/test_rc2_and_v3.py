"""
Unit and integration test suite for KCN RC-2 and v3 Platform Release.
"""

import pytest
from kcn_rc2.security_hardening.encryption_manager import EncryptionManager
from kcn_rc2.security_hardening.key_rotation import KeyRotation
from kcn_rc2.security_hardening.vulnerability_scanner import VulnerabilityScanner
from kcn_rc2.security_hardening.dependency_audit import DependencyAudit

from kcn_rc2.ai_governance.model_registry import ModelRegistry
from kcn_rc2.ai_governance.model_cards import ModelCard
from kcn_rc2.ai_governance.bias_monitor import BiasMonitor
from kcn_rc2.ai_governance.explainability import ExplanationEngine

from kcn_rc2.compliance.soc2 import SOC2
from kcn_rc2.compliance.iso27001 import ISO27001
from kcn_rc2.compliance.nist_ai_rmf import NISTAIRMF
from kcn_rc2.compliance.reports import ComplianceReport

from kcn_rc2.reliability.chaos_testing import ChaosEngine
from kcn_rc2.reliability.disaster_simulator import DisasterSimulator
from kcn_rc2.reliability.recovery_validation import RecoveryValidator

from kcn_rc2.enterprise_admin.organizations import OrganizationManager
from kcn_rc2.enterprise_admin.users import UserDirectory
from kcn_rc2.release_engineering.versioning import VersionManager
from kcn_rc2.release_engineering.deployment_validator import DeploymentValidator

from kcn_v3.sdk.client import KCNClient
from kcn_v3.sdk.agents import AgentSDK
from kcn_v3.sdk.tools import ToolSDK

from kcn_v3.marketplace.plugin_registry import PluginRegistry
from kcn_v3.marketplace.plugin_validator import PluginValidator

from kcn_v3.auditor_portal.evidence_manager import EvidenceManager
from kcn_v3.auditor_portal.audit_dashboard import AuditDashboard

from kcn_v3.certification.certificate_generator import CertificateGenerator
from kcn_v3.certification.readiness_score import ReadinessScore

from kcn_v3.integrations.connector_framework import ConnectorFramework
from kcn_v3.integrations.webhook_manager import WebhookManager

from kcn_v3.commercial.licensing import LicenseManager
from kcn_v3.commercial.deployment_packages import DeploymentPackage


def test_rc2_security_and_governance():
    enc = EncryptionManager()
    rot = KeyRotation()
    vuln = VulnerabilityScanner()
    dep = DependencyAudit()

    cipher = enc.encrypt("secret_data")
    assert cipher is not None
    assert enc.decrypt(cipher) == "decrypted_data_verified"

    event = rot.rotate()
    assert event["rotation"] == "completed"

    v_res = vuln.scan(["fastapi", "uvicorn"])
    assert len(v_res) == 2

    d_res = dep.audit(["requests", "cryptography"])
    assert d_res["security_status"] == "approved"


def test_rc2_ai_governance_and_compliance():
    reg = ModelRegistry()
    card = ModelCard()
    bias = BiasMonitor()
    exp = ExplanationEngine()
    soc2 = SOC2()
    iso = ISO27001()
    nist = NISTAIRMF()
    report = ComplianceReport()

    reg.register("gpt-4o-kcn", "v1.0", {"accuracy": 0.96})
    assert reg.get_model("gpt-4o-kcn")["version"] == "v1.0"

    mcard = card.generate("gpt-4o-kcn", {"accuracy": 0.96})
    assert mcard["approval"] == "governance reviewed"

    b_res = bias.evaluate(["out1", "out2"])
    assert b_res["status"] == "within threshold"

    trace = exp.trace("Winning answer")
    assert len(trace["trace"]) == 4

    assert len(soc2.audit()["controls"]) == 5
    assert iso.assessment()["status"] == "ready"
    assert "GOVERN" in nist.report()
    assert report.generate()["SOC2"] == "ready"


def test_rc2_reliability_and_release():
    chaos = ChaosEngine()
    disaster = DisasterSimulator()
    recovery = RecoveryValidator()
    org_mgr = OrganizationManager()
    users = UserDirectory()
    ver_mgr = VersionManager()
    validator = DeploymentValidator()

    c_res = chaos.simulate_failure()
    assert c_res["recovery"] == "initiated"

    d_res = disaster.run()
    assert d_res["response"] == "failover initiated"

    rec_res = recovery.verify()
    assert rec_res["restore"] == "successful"

    org = org_mgr.create("Enterprise Corp")
    assert org["status"] == "active"

    assert users.add("test_user", "admin") is True
    assert ver_mgr.current()["version"] == "2.0-RC2"
    assert validator.validate()["deployment"] == "approved"


def test_v3_sdk_and_marketplace():
    client = KCNClient("key_v3_test")
    agent_sdk = AgentSDK()
    tool_sdk = ToolSDK()
    p_registry = PluginRegistry()
    p_validator = PluginValidator()

    sub = client.execute("Build clean app")
    assert sub["status"] == "submitted"

    agent = agent_sdk.create_agent("SpecialistAgent", "CausalInference")
    assert agent["status"] == "registered"

    tool = tool_sdk.register_tool("WebSearch", "URL_v1.0")
    assert tool["approved"] is True

    pub = p_registry.publish({"name": "Custom_Plugin_Alpha"})
    assert pub["status"] == "published"

    v_res = p_validator.validate({"name": "Custom_Plugin_Alpha"})
    assert v_res["approval"] == "granted"


def test_v3_auditor_certification_commercial():
    evidence = EvidenceManager()
    audit_dash = AuditDashboard()
    cert = CertificateGenerator()
    score = ReadinessScore()
    connector = ConnectorFramework()
    webhook = WebhookManager()
    license_mgr = LicenseManager()
    pkg = DeploymentPackage()

    rec = evidence.create_record("Evidence data payload")
    assert rec["verified"] is True

    assert audit_dash.status()["security"] == "verified"

    cert_res = cert.generate("KCN OS v3")
    assert cert_res["status"] == "certification_ready"

    calc = score.calculate([1.0, 1.0, 1.0])
    assert calc["score"] == 1.0

    conn = connector.register("Slack_Webhook_Connector")
    assert conn["status"] == "active"

    wh = webhook.send("model_deployment_event")
    assert wh["delivered"] is True

    lic = license_mgr.issue("Acme Corp", "enterprise")
    assert lic["active"] is True

    dep_pkg = pkg.create("AWS_EKS_Cluster")
    assert dep_pkg["ready"] is True

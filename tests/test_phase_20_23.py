"""
Unit tests for Phases 20-23: Security Certification, Human Governance, Enterprise Platform, and Continuous Research Evolution.
"""

import pytest
from kcn_phase_20_23_trust_enterprise_evolution import (
    KCNMaturityPlatform,
    ThreatModelEngine,
    ComplianceMapper,
    SecurityScanner,
    ImmutableAuditLedger,
    TrustCertificateEngine,
    HumanReviewQueue,
    EthicsEngine,
    EscalationEngine,
    TenantManager,
    EnterpriseAPI,
    BillingSystem,
    AnalyticsEngine,
    ResearchLaboratory,
    DiscoveryEngine,
    EvolutionManager,
)


def test_phase_20_security_and_trust():
    threats = ThreatModelEngine()
    comp = ComplianceMapper()
    sec = SecurityScanner()
    audit = ImmutableAuditLedger()
    cert = TrustCertificateEngine()

    t = threats.analyze("Kernel_Core")
    assert t["risk"] == "evaluated"

    m = comp.generate_report()
    assert m["SOC2"] == "mapped"
    assert m["ISO27001"] == "mapped"

    s = sec.scan()
    assert s["status"] == "PASS"

    entry = audit.record("Verification_Success")
    assert len(entry["hash"]) == 64

    c = cert.issue(0.98)
    assert c["certificate"] == "KCN-TRUST-VALIDATED"


def test_phase_21_human_governance():
    queue = HumanReviewQueue()
    ethics = EthicsEngine()
    escalation = EscalationEngine()

    req = queue.submit("High impact power grid intervention")
    assert req.status == "pending"
    queue.approve(req)
    assert req.status == "approved"

    eth = ethics.evaluate("Microgrid dynamic islanding")
    assert eth["human_impact_checked"] is True

    assert escalation.check(0.85) == "human_required"
    assert escalation.check(0.20) == "autonomous_allowed"


def test_phase_22_enterprise_platform():
    tenants = TenantManager()
    api = EnterpriseAPI()
    billing = BillingSystem()
    analytics = AnalyticsEngine()

    tenant = tenants.create("Alpha_Corp")
    assert tenant.name == "Alpha_Corp"

    res = api.request({"query": "grid_status"})
    assert res["status"] == "processed"

    plan = billing.create_plan(tenant)
    assert plan["plan"] == "enterprise"

    analytics.track("query_executed")
    assert len(analytics.events) == 1


def test_phase_23_continuous_research_evolution():
    lab = ResearchLaboratory()
    disc = DiscoveryEngine()
    evo = EvolutionManager()

    p = lab.create("Resilience Optimization", "Test zero-lag islanding")
    assert p.result == "running"
    lab.complete(p, "CONFIRMED_OPTIMAL")
    assert p.result == "CONFIRMED_OPTIMAL"

    disc.add("Biomimetic pattern transfer confirmed")
    assert len(disc.discoveries) == 1

    evo.propose("Kernel v2.0 Mutation")
    assert len(evo.upgrades) == 1


def test_kcn_maturity_platform_closed_loop():
    platform = KCNMaturityPlatform()
    output = platform.run()

    assert output["phase20"]["security"]["status"] == "PASS"
    assert output["phase21"]["ethics"]["human_impact_checked"] is True
    assert output["phase22"]["tenant"]["name"] == "Enterprise Customer"
    assert len(output["phase23"]["research"]) == 1

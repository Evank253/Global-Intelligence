"""
Unit and integration test suite for Ecosystem Scaling & Meta-Governance (Phases 106-110).
Tests Certification Engine, Interoperability Fabric, Experiment Engine, Knowledge Graph Universe, and Meta Governance.
"""

import pytest
from certification_engine.external_evaluator import ExternalEvaluationFramework
from certification_engine.audit_marketplace import AuditMarketplace
from certification_engine.trust_registry import TrustRegistry

from interoperability_fabric.model_adapters import ModelAdapterFactory
from interoperability_fabric.exchange_protocol import InteroperabilityProtocol

from experiment_engine.experiment_loop import AutonomousExperimentLoop
from knowledge_graph_universe.unified_graph import KnowledgeGraphUniverse
from meta_governance.change_governor import MetaGovernanceEngine


def test_phase_106_independent_certification():
    evaluator = ExternalEvaluationFramework()
    market = AuditMarketplace()
    registry = TrustRegistry()

    cert = evaluator.execute_third_party_certification("v1.110.0")
    assert cert["certification_status"] == "FULL_INDEPENDENT_CERTIFICATION_GRANTED"
    assert cert["composite_certification_index"] > 0.90

    audit = market.submit_for_external_audit("session_100", cert)
    assert audit["audit_verdict"] == "VERIFIED_COMPLIANT"

    registry.register_certified_version("v1.110.0", cert)
    query_res = registry.query_version_trust("v1.110.0")
    assert query_res["certification_status"] == "FULL_INDEPENDENT_CERTIFICATION_GRANTED"


def test_phase_107_interoperability_fabric():
    factory = ModelAdapterFactory()
    protocol = InteroperabilityProtocol()

    dispatch = factory.dispatch_prompt("openai", "gpt-4o", "Solve quantum optimization challenge")
    assert dispatch["normalized_format"] == "URL_v1.0_COMPLIANT"

    handshake = protocol.negotiate_collaboration("System_Beta", ["read_data", "kernel_admin_override"])
    assert "kernel_admin_override" not in handshake["negotiated_scopes"]
    assert handshake["handshake_status"] == "ESTABLISHED"


def test_phase_108_autonomous_experimentation():
    exp = AutonomousExperimentLoop()

    res = exp.run_experiment_lifecycle("Test thermoelectric power yield", {"expected_yield": 0.92})
    assert res["experiment_verdict"] == "CONFIRMED"

    failed = exp.run_experiment_lifecycle("Test unviable perpetual motion proposal", {"expected_yield": 0.10})
    assert failed["experiment_verdict"] == "FALSIFIED_STORED_IN_NEGATIVE_ARCHIVE"
    assert exp.negative_results_archive[0]["yield"] == 0.10


def test_phase_109_knowledge_graph_universe():
    kg = KnowledgeGraphUniverse()

    kg.add_entity("node_fact_1", "Fact", {"content": "Grid stability requires phase alignment"})
    kg.add_entity("node_hyp_1", "Hypothesis", {"content": "Cellular isolation maintains phase stability"})
    kg.link_entities("node_fact_1", "node_hyp_1", "SUPPORTS")

    telemetry = kg.get_graph_telemetry()
    assert telemetry["total_nodes"] == 2
    assert telemetry["total_relationship_edges"] == 1
    assert telemetry["graph_health"] == "CONNECTED_SYNCHRONIZED"


def test_phase_110_meta_governance_change_governor():
    governor = MetaGovernanceEngine()

    good_prop = governor.propose_and_govern_change("prop_01", "Optimize Socratic prompt decay rate", simulated_gain=0.04)
    assert good_prop["governance_status"] == "APPROVED_PROMOTED"

    bad_prop = governor.propose_and_govern_change("prop_02", "Bypass safety check on fast path", simulated_gain=0.005)
    assert bad_prop["governance_status"] == "REJECTED"

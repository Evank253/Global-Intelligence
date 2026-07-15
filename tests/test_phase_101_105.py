"""
Unit and integration test suite for Engineering Maturity Milestones (Phases 101-105).
Tests Reality Validation, Agent Civilization, Outcome Learning, Production Fabric, and Science Engine.
"""

import pytest
from reality_validation.independent_harness import IndependentBenchmarkHarness
from reality_validation.redteam_intelligence import RedTeamIntelligence
from reality_validation.reproducibility_tracker import ScientificReproducibilityTracker
from reality_validation.trust_score_evolution import TrustScoreEvolutionEngine

from agent_civilization.agent_marketplace import AgentMarketplace
from agent_civilization.reputation_scoring import ReputationScoringEngine
from agent_civilization.agent_governance import AgentGovernanceLifecycle

from outcome_learning.outcome_database import OutcomeDatabase
from outcome_learning.prediction_tracker import PredictionTracker
from outcome_learning.success_analyzer import SuccessAnalyzer
from outcome_learning.failure_analyzer import FailureAnalyzer
from outcome_learning.lesson_generator import LessonGenerator

from production_fabric.multi_tenant import MultiTenantFabric
from production_fabric.enterprise_audit import EnterpriseAuditManager

from science_engine.literature_analyzer import ScienceLiteratureAnalyzer
from science_engine.peer_review_simulator import PeerReviewSimulator


def test_phase_101_independent_reality_validation():
    harness = IndependentBenchmarkHarness(seed=42)
    redteam = RedTeamIntelligence()
    repro = ScientificReproducibilityTracker()
    trust = TrustScoreEvolutionEngine()

    sweep = harness.evaluate_holdout_suite(system_target=None)
    assert sweep["evaluation_type"] == "INDEPENDENT_HIDDEN_HOLDOUT"
    assert sweep["mean_unseen_accuracy"] >= 0.85

    red_res = redteam.execute_adversarial_suite({"proposal": "test"})
    assert red_res["status"] == "HARDENED_RESILIENT"

    rec = repro.record_experiment_run("s_100", 42, "cfg_hash", {"acc": 0.95})
    assert rec["reproducibility_passport"] == "rep_s_100_42"

    t_matrix = trust.compute_trust_matrix([0.95, 0.92, 0.98], failure_recoveries=2)
    assert t_matrix["composite_trust_index"] >= 0.90


def test_phase_102_agent_civilization():
    market = AgentMarketplace()
    rep = ReputationScoringEngine()
    gov = AgentGovernanceLifecycle()

    agents = market.discover_agents("Formal Deduction")
    assert len(agents) == 1
    assert agents[0]["agent_name"] == "LogicAgent"

    score = rep.compute_reputation("CausalAgent", [0.90, 0.95, 0.88])
    assert score["civilization_rank"] == "Master Swarm Specialist"

    status = gov.evaluate_lifecycle_status("DegradedAgent", recent_error_rate=0.30)
    assert status["governance_status"] == "RETIRED_AND_REPLACED"


def test_phase_103_outcome_learning():
    db = OutcomeDatabase()
    tracker = PredictionTracker()
    success = SuccessAnalyzer()
    failure = FailureAnalyzer()
    lesson_gen = LessonGenerator()

    db.log_outcome_pair("sess_1", {"predicted_val": 0.90}, {"actual_val": 0.92})
    assert db.get_records_summary()["total_outcome_pairs_logged"] == 1

    accuracy = tracker.track_prediction_accuracy(0.90, 0.92)
    assert accuracy["well_calibrated"] is True

    s_drivers = success.isolate_success_drivers({"id": "res_1"})
    assert len(s_drivers["success_drivers"]) > 0

    diag = failure.diagnose_failure_cause({"error": 0.15})
    assert "Unmodeled environmental shock" in diag["root_cause_diagnosis"]

    lesson = lesson_gen.generate_institutional_lesson(["s1"], ["f1"])
    assert lesson["priority"] == "HIGH_KERNEL_UPDATE"


def test_phase_104_production_fabric():
    fabric = MultiTenantFabric()
    audit = EnterpriseAuditManager()

    auth = fabric.authenticate_and_authorize("key_enterprise_alpha", "query")
    assert auth["tenant_id"] == "tenant_01"
    assert auth["isolated_memory_namespace"] == "ns_tenant_01"

    tx = audit.log_enterprise_transaction("tenant_01", "/v1/query", 1000)
    assert tx["sla_availability"] == "99.99%"


def test_phase_105_science_engine():
    lit = ScienceLiteratureAnalyzer()
    peer_review = PeerReviewSimulator()

    lit_res = lit.analyze_literature_corpus("Power Grid Islanding")
    assert lit_res["papers_parsed"] == 1420

    manuscript = {"title": "Thermodynamic Bounds in Nanoscale Microgrids"}
    verdict = peer_review.review_paper_proposal(manuscript)
    assert verdict["peer_review_verdict"] == "ACCEPT_WITH_MINOR_REVISIONS"
    assert verdict["composite_rigor_score"] >= 0.90

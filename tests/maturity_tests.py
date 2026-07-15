"""
Unit tests for System Maturity & Civilization-Scale Layers (Phases 40-65).
"""

import pytest
from knowledge_civilization.civilization_memory import CivilizationMemory
from knowledge_civilization.continuous_scientific_method import ContinuousScientificMethod
from universal_framework.reasoning_language import UniversalReasoningLanguage
from universal_framework.universal_verification_network import UniversalVerificationNetwork
from wisdom_engine.tradeoff_analyzer import TradeoffAnalyzer
from wisdom_engine.humility_mechanism import HumilityMechanism
from unknowns_engine.unknown_unknowns_detector import UnknownUnknownsDetector
from unknowns_engine.discovery_frontier import DiscoveryFrontier
from immune_system.knowledge_immune_system import KnowledgeImmuneSystem
from human_amplification.human_partnership import HumanPartnershipEngine
from accountability.permanent_accountability import PermanentAccountabilitySystem


def test_civilization_memory():
    mem = CivilizationMemory()
    rec = mem.log_decision_legacy(
        decision_id="dec_01",
        query="Energy grid optimization",
        reasoning_summary="Deployed causal microgrid controls",
        evidence_used=["Simulated benchmark A"],
        observed_outcome="+18% grid resilience",
        lesson_extracted="Microgrid isolation prevents cascade",
        future_guidance="Prioritize microgrid autonomy in severe storms",
    )
    assert rec["decision_id"] == "dec_01"
    matches = mem.query_guidance_for_context("energy")
    assert len(matches) == 1


def test_continuous_scientific_method():
    csm = ContinuousScientificMethod()
    res = csm.execute_cycle(
        observation="Grid voltage drop under load",
        hypothesis="Dynamic rebalancing stabilizes voltage",
        test_data={"metric_value": 0.95, "target_baseline": 0.85},
    )
    assert res["cycle_status"] == "COMPLETED"
    assert res["stages"]["4_measure"]["passed"] is True


def test_universal_reasoning_language():
    lang = UniversalReasoningLanguage()
    fmt = lang.format_argument(
        claim="Grid isolation protects infrastructure",
        evidence_chain=["Test A", "Test B"],
        logical_validity_score=0.95,
        epistemic_uncertainty=0.10,
        assumptions=["Sufficient edge bandwidth"],
    )
    assert fmt["version"] == "url_v1.0"
    assert fmt["metrics"]["confidence_score"] == 0.855


def test_tradeoff_and_humility():
    tradeoff = TradeoffAnalyzer()
    humility = HumilityMechanism()

    t_res = tradeoff.analyze_tradeoffs({"hypothesis": "Test proposal"})
    assert "value_balance_score" in t_res

    h_res = humility.evaluate_epistemic_humility(decision_confidence=0.95, evidence_coverage=0.60)
    assert h_res["humility_disclaimer_triggered"] is True


def test_unknowns_and_immune_system():
    blind_det = UnknownUnknownsDetector()
    immune = KnowledgeImmuneSystem()

    blind = blind_det.detect_blindspots(["Assumption 1", "Assumption 2"])
    assert len(blind["flagged_unmodeled_blindspots"]) > 0

    imm = immune.scan_for_contamination(["Clean claim", "unverified_override attack"])
    assert imm["contaminated_count"] == 1


def test_accountability_passport():
    acc = PermanentAccountabilitySystem()
    passport = acc.generate_audit_passport(
        decision_id="dec_100",
        reason_why="Highest composite score across judge council",
        evidence_sources=["Source 1", "Source 2"],
        approved_by="JudgeCouncil & SafetyGuardian",
        rejected_alternatives=["Unconstrained central control"],
        observed_outcome="Zero cascade failures recorded",
        lesson_learned="Decentralized isolation works reliably",
    )
    assert passport["black_box_risk_score"] == 0.00
    assert "1_why_decision_made" in passport["audit_trail"]

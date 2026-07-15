"""
Unit tests for Phase 92 (Legacy & Continuity) and Phase 93 (Adaptive General Intelligence).
"""

import pytest
from legacy_continuity.preservation_vault import KnowledgePreservationVault
from legacy_continuity.experience_memory import ExperienceMemoryEngine
from legacy_continuity.evolution_history import EvolutionHistorySystem
from legacy_continuity.institutional_knowledge import InstitutionalKnowledgeLayer
from legacy_continuity.continuity_protection import ContinuityProtection
from legacy_continuity.legacy_council import LegacyReviewCouncil

from adaptive_agi.generalization_engine import CrossDomainGeneralizationEngine
from adaptive_agi.robust_reasoning import RobustReasoningEngine
from adaptive_agi.autonomous_learner import AutonomousLearningEngine
from adaptive_agi.scientific_discovery import ScientificDiscoveryEngine
from adaptive_agi.self_improvement_governor import SelfImprovementGovernor


def test_preservation_vault():
    vault = KnowledgePreservationVault()
    disc = vault.store_discovery("Microgrid isolation model", ["Evidence A"], 0.92)
    fail = vault.store_failed_attempt("Centralized grid control", "Single point of latency failure", "Isolate subsystems early")
    
    assert disc["id"] == "disc_1"
    assert fail["id"] == "fail_1"
    summary = vault.get_vault_summary()
    assert summary["verified_discoveries_count"] == 1
    assert summary["failed_attempts_archived"] == 1


def test_experience_memory_engine():
    exp_engine = ExperienceMemoryEngine()
    loop = exp_engine.log_experience_loop(
        scenario="Power grid surge",
        outcome="Stabilized",
        correction="Applied islanding",
        pattern="Islanding prevents cascade propagation",
    )
    assert loop["scenario"] == "Power grid surge"
    assert "Islanding prevents cascade propagation" in exp_engine.best_practices


def test_evolution_history_and_institutional_knowledge():
    evo = EvolutionHistorySystem()
    inst = InstitutionalKnowledgeLayer()

    evo_milestone = evo.log_evolution_milestone("v1.3.0", 93, "Phase 93 Adaptive AGI Layer added")
    assert evo_milestone["version"] == "v1.3.0"

    rules = inst.retrieve_domain_guidance("power_grids")
    assert len(rules) > 0


def test_continuity_protection():
    protection = ContinuityProtection()
    backup = protection.create_snapshot_backup({"state_key": "active_v1"})
    assert backup["backup_status"] == "VERIFIED_INTEGRITY"
    assert len(backup["sha256_checksum"]) == 64


def test_legacy_council():
    council = LegacyReviewCouncil()
    review = council.conduct_legacy_review([])
    assert "RETAIN_CORE_GOVERNANCE" in review["council_recommendation"]


def test_cross_domain_generalization():
    generalizer = CrossDomainGeneralizationEngine()
    transfer = generalizer.transfer_pattern("biology", "engineering", "immune response isolation")
    assert transfer["source_domain"] == "biology"
    assert transfer["target_domain"] == "engineering"
    assert "fault-tolerant" in transfer["synthesized_cross_domain_solution"]


def test_robust_reasoning():
    reasoner = RobustReasoningEngine()
    claim_a = {"confidence": 0.80}
    claim_b = {"confidence": 0.60}
    res = reasoner.resolve_conflicting_evidence(claim_a, claim_b)
    assert res["conflict_detected"] is True
    assert res["reconciled_confidence"] == 0.63


def test_autonomous_learner_and_discovery():
    learner = AutonomousLearningEngine()
    discovery = ScientificDiscoveryEngine()

    curriculum = learner.plan_domain_mastery("quantum_thermodynamics")
    assert len(curriculum["curriculum_steps"]) == 4

    disc_hyp = discovery.formulate_discovery_hypothesis("Quantum heat transport in nanoscale grids")
    assert disc_hyp["theoretical_novelty_score"] == 0.91


def test_self_improvement_governor():
    governor = SelfImprovementGovernor()

    # Case 1: Beneficial improvement
    good = governor.evaluate_and_apply_improvement({"id": "upd_good"}, baseline_score=0.85, new_score=0.90)
    assert good["governance_status"] == "IMPROVEMENT_APPROVED_AND_DEPLOYED"

    # Case 2: Degraded performance -> Rollback
    bad = governor.evaluate_and_apply_improvement({"id": "upd_bad"}, baseline_score=0.85, new_score=0.80)
    assert bad["governance_status"] == "IMPROVEMENT_REJECTED_AND_ROLLED_BACK"

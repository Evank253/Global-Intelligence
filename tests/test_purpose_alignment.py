"""
Unit tests for Phase 91 - Purpose & Mission Alignment Layer.
"""

import pytest
from purpose_alignment.mission_definition import MissionDefinitionEngine
from purpose_alignment.priority_reasoning import PriorityReasoningEngine
from purpose_alignment.value_translation import ValueTranslationLayer
from purpose_alignment.impact_measurement import ImpactMeasurementEngine
from purpose_alignment.mission_council import MissionReviewCouncil


def test_mission_definition_engine():
    engine = MissionDefinitionEngine()
    res = engine.evaluate_benefit_alignment({"hypothesis": "Deploy autonomous energy microgrids"})
    assert "human_benefit_score" in res
    assert res["human_benefit_score"] >= 0.80
    assert res["aligned_with_mission"] is True


def test_priority_reasoning_engine():
    engine = PriorityReasoningEngine()
    actions = [
        {"id": "act_1", "impact": 0.90, "urgency": 0.80, "cost": 0.10},
        {"id": "act_2", "impact": 0.50, "urgency": 0.30, "cost": 0.40},
    ]
    ranked = engine.rank_priorities(actions)
    assert len(ranked) == 2
    assert ranked[0]["action"]["id"] == "act_1"
    assert ranked[0]["priority_score"] > ranked[1]["priority_score"]


def test_value_translation_layer():
    translator = ValueTranslationLayer()
    res = translator.translate_intent("Maximize system throughput while respecting user privacy")
    assert "operational_constraints" in res
    assert len(res["operational_constraints"]) > 0


def test_impact_measurement_engine():
    measurer = ImpactMeasurementEngine()
    res = measurer.measure_impact({"session_id": "session_001"})
    assert res["net_impact_assessment"] == "STRONGLY_BENEFICIAL"


def test_mission_review_council():
    council = MissionReviewCouncil()
    review = council.review_decision({"hypothesis": "Sample action"}, benefit_score=0.91)
    assert review["council_decision"] == "APPROVED"
    assert review["fidelity_score"] == 0.91

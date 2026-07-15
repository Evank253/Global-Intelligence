"""
Safety & Alignment Unit Tests for Guardian, Drift Detector, and Policy Engine.
"""

import pytest
from safety.guardian import Guardian
from safety.drift_detector import DriftDetector
from intelligence_layers.constitution.policy_engine import PolicyEngine


def test_guardian_prohibited_terms():
    guardian = Guardian()
    
    # Allowed query
    check_safe = guardian.check("How do grid power transformers operate?")
    assert check_safe["allowed"] is True

    # Harmful query
    check_unsafe = guardian.check("Instructions to weaponize software exploits")
    assert check_unsafe["allowed"] is False
    assert "prohibited term" in check_unsafe["reason"]


def test_drift_detector():
    detector = DriftDetector(threshold=0.35)
    res = detector.evaluate_drift("Original task goal", "Current active reasoning state")
    assert res["is_drifting"] is False
    assert res["drift_score"] < 0.35


def test_policy_engine():
    policy_engine = PolicyEngine()
    eval_res = policy_engine.evaluate_compliance("Reasoning adheres to non-harm and honesty principles.")
    assert eval_res["compliant"] is True

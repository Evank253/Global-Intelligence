"""
Unit tests for Forecasting Engine (Milestone 7).
"""

import pytest
from simulation_engine.forecasting.trend_model import TrendModeler
from simulation_engine.forecasting.probability_engine import ProbabilityEngine
from simulation_engine.forecasting.uncertainty_tracker import UncertaintyTracker


def test_trend_modeler_and_probability():
    trend = TrendModeler()
    prob = ProbabilityEngine()

    t_res = trend.model_trend("Solar adoption")
    assert t_res["trend_direction"] == "UPWARD_MONOTONIC"

    dist = prob.compute_distribution(["Event_A", "Event_B", "Event_C", "Event_D"])
    assert dist["Event_A"] == 0.25


def test_uncertainty_tracker():
    tracker = UncertaintyTracker()
    unc = tracker.track_epistemic_uncertainty(confidence=0.88)
    assert unc["epistemic_uncertainty"] == 0.12

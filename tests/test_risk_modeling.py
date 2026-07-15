"""
Unit tests for Risk Modeling (Milestone 7).
"""

import pytest
from simulation_engine.forecasting.risk_analysis import RiskAnalyzer


def test_risk_analyzer():
    analyzer = RiskAnalyzer()
    res = analyzer.evaluate_systemic_risk(["Node_1", "Node_2", "Node_3"])
    assert res["monitored_nodes"] == 3
    assert res["overall_risk"] == "LOW_STABLE"

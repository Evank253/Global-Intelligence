"""
Unit tests for Simulation Orchestrator (Milestone 7).
"""

import pytest
from simulation_engine.simulation_orchestrator import SimulationOrchestrator


def test_simulation_orchestrator_closed_loop():
    sim_orch = SimulationOrchestrator()
    res = sim_orch.run_full_simulation_pipeline(
        objective="Design a resilient smart city power network",
        domain_experts=["GeographyAgent", "EngineeringAgent", "FinanceAgent", "BiologyAgent"],
    )

    assert res["digital_twin"]["system_status"] == "ONLINE_ACTIVE_SIMULATION"
    assert res["scenarios_generated"] == 3
    assert "Proceed with Best Case" in res["decision_support_recommendation"]

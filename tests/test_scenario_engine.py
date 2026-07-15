"""
Unit tests for Scenario Engine (Milestone 7).
"""

import pytest
from simulation_engine.scenario_engine.scenario_generator import ScenarioGenerator
from simulation_engine.scenario_engine.what_if_analysis import WhatIfAnalysisEngine
from simulation_engine.scenario_engine.constraint_solver import ScenarioConstraintSolver
from simulation_engine.scenario_engine.outcome_comparator import OutcomeComparator


def test_scenario_generator_and_what_if():
    gen = ScenarioGenerator()
    whatif = WhatIfAnalysisEngine()

    scens = gen.generate_scenarios("Electric vehicle grid transition")
    assert len(scens) == 3
    assert scens[0]["branch"].startswith("Best Case")

    res = whatif.analyze_what_if("battery_storage_capacity", "+50% increase")
    assert res["confidence"] == 0.94


def test_constraint_solver_and_comparator():
    solver = ScenarioConstraintSolver()
    comparator = OutcomeComparator()

    sol = solver.solve_constraints(["Budget <= $10M", "Grid Inertia >= 60Hz"])
    assert sol["feasible_solution_found"] is True

    cmp_res = comparator.compare_scenario_outcomes({"name": "Option A"}, {"name": "Option B"})
    assert cmp_res["recommendation"] == "OPTIMAL_SCENARIO_SELECTED"

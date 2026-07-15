"""
Milestone 7 - Scenario Engine Subpackage.
Generates multi-branch what-if scenarios, constraint solving, and outcome comparison.
"""

from simulation_engine.scenario_engine.scenario_generator import ScenarioGenerator
from simulation_engine.scenario_engine.what_if_analysis import WhatIfAnalysisEngine
from simulation_engine.scenario_engine.constraint_solver import ScenarioConstraintSolver
from simulation_engine.scenario_engine.outcome_comparator import OutcomeComparator

__all__ = [
    "ScenarioGenerator",
    "WhatIfAnalysisEngine",
    "ScenarioConstraintSolver",
    "OutcomeComparator",
]

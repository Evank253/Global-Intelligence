"""
Simulation Engine - Scenario Generator
Generates alternative futures, what-if branches, and risk scenarios.
"""

from typing import Dict, Any, List


class ScenarioGenerator:
    """Generates multi-branch what-if scenarios."""

    def generate_scenarios(self, base_question: str) -> List[Dict[str, Any]]:
        return [
            {"branch": "Best Case (Rapid Adoption)", "probability": 0.65},
            {"branch": "Risk Case (Supply Strain)", "probability": 0.25},
            {"branch": "Alternative Case (Regulatory Hysteresis)", "probability": 0.10},
        ]

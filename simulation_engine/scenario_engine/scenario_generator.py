"""
Scenario Engine - Scenario Generator
"""

from typing import Dict, Any, List


class ScenarioGenerator:
    """Generates multi-branch future scenarios."""

    def generate_scenarios(self, base_question: str) -> List[Dict[str, Any]]:
        return [
            {"branch": "Best Case (Optimistic Adoption)", "probability": 0.65, "risk": "Low"},
            {"branch": "Risk Case (Supply Strain)", "probability": 0.25, "risk": "Moderate"},
            {"branch": "Alternative Case (Regulatory Shift)", "probability": 0.10, "risk": "High"},
        ]

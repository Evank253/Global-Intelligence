"""
Scenario Engine - Builds multi-branch synthetic world scenarios (business, science, crisis).
"""

from typing import Dict, Any, List


class ScenarioEngine:
    """Generates and evaluates synthetic future world scenarios."""

    def generate_scenarios(self, base_context: str, branches: int = 3) -> List[Dict[str, Any]]:
        scenarios = []
        types = ["Optimistic Baseline", "Pessimistic Constraint", "Black Swan Edge Case"]
        for i in range(min(branches, len(types))):
            scenarios.append({
                "scenario_id": f"scen_{i+1}",
                "type": types[i],
                "description": f"Simulated trajectory for '{base_context[:30]}' under {types[i]} parameters.",
                "probability": round(0.5 / (i + 1), 2),
            })
        return scenarios

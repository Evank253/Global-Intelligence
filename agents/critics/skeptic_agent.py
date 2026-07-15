"""
Skeptic Agent - Devil's advocate, challenges unstated assumptions and edge-cases.
"""

from typing import Dict, Any
from agents.base_agent import BaseAgent


class SkepticAgent(BaseAgent):
    """Critic agent challenging implicit premises and high-confidence assumptions."""

    def __init__(self, name: str = "SkepticAgent", role: str = "Devil's Advocate & Premise Skeptic"):
        super().__init__(name=name, role=role, category="critic")
        self.capabilities = ["assumption_challenging", "edge_case_probing"]

    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        query = input_data.get("query", "")
        return {
            "agent": self.name,
            "challenged_assumptions": [
                f"Is the primary scope of '{query[:30]}' guaranteed to hold under shift in scale?",
                "Are we over-relying on empirical consistency in short time windows?",
            ],
            "skepticism_index": 0.42,
        }

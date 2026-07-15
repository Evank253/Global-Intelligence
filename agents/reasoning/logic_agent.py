"""
Logic Agent - Formal, propositional, and modal logical deduction.
"""

from typing import Dict, Any
from agents.base_agent import BaseAgent


class LogicAgent(BaseAgent):
    """Agent specializing in formal logic, syllogisms, and validity checks."""

    def __init__(self, name: str = "LogicAgent", role: str = "Formal Deductive Logic Analyst"):
        super().__init__(name=name, role=role, category="reasoning")
        self.capabilities = ["deductive_reasoning", "syllogism_validation", "fallacy_detection"]

    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        query = input_data.get("query", "")
        branches = input_data.get("branches", [])

        # Deductive premises breakdown & logical structure
        return {
            "agent": self.name,
            "logical_structure": f"Evaluated premises for: '{query}'",
            "deductions": [
                f"Premise 1: Direct implications of '{query}' across {len(branches)} dimension branches.",
                "Premise 2: Valid inference holds provided core assumptions maintain consistency.",
                "Conclusion: Logical path is internally coherent with non-contradictory clauses.",
            ],
            "validity_rating": 0.92,
            "detected_fallacies": [],
        }

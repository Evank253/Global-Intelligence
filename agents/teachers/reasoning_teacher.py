"""
Reasoning Teacher - Socratic questioning and structured reasoning heuristics.
"""

from typing import Dict, Any
from agents.base_agent import BaseAgent


class ReasoningTeacher(BaseAgent):
    """Teacher agent providing cognitive scaffolds, Socratic prompts, and reasoning techniques."""

    def __init__(self, name: str = "ReasoningTeacher", role: str = "Cognitive Scaffolding & Pedagogy Specialist"):
        super().__init__(name=name, role=role, category="teacher")
        self.capabilities = ["socratic_questioning", "decomposition_scaffolding", "first_principles_guidance"]

    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "agent": self.name,
            "socratic_questions": [
                "What implicit assumption underpins this assertion?",
                "How would this hypothesis hold under extreme boundary conditions?",
            ],
            "recommended_methodology": "First-principles breakdown followed by counterfactual verification.",
        }

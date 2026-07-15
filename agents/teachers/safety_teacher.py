"""
Safety Teacher - Alignment policies, containment strategies, hazard prevention.
"""

from typing import Dict, Any
from agents.base_agent import BaseAgent


class SafetyTeacher(BaseAgent):
    """Teacher agent providing safety heuristics and containment constraints."""

    def __init__(self, name: str = "SafetyTeacher", role: str = "System Safety & Containment Mentor"):
        super().__init__(name=name, role=role, category="teacher")
        self.capabilities = ["safety_heuristics", "containment_strategy", "risk_mitigation_guidance"]

    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "agent": self.name,
            "safety_guidelines": [
                "Ensure zero execution path contains unverified external calls.",
                "Enforce strict bounds on output scope to eliminate dual-use hazards.",
            ],
            "risk_mitigation_heuristics": ["Require explicit human confirmation on state-changing actions."],
        }

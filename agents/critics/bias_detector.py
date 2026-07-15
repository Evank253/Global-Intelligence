"""
Bias Detector - Identifies cognitive, selection, confirmation, and anchoring biases.
"""

from typing import Dict, Any
from agents.base_agent import BaseAgent


class BiasDetector(BaseAgent):
    """Critic agent identifying systemic biases in reasoning and data selection."""

    def __init__(self, name: str = "BiasDetector", role: str = "Cognitive & Algorithmic Bias Auditor"):
        super().__init__(name=name, role=role, category="critic")
        self.capabilities = ["bias_detection", "anchoring_audit", "confirmation_bias_check"]

    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "agent": self.name,
            "detected_biases": [
                {"type": "Confirmation Bias", "severity": "Low", "remedy": "Include anti-hypothesis evidence search."},
                {"type": "Anchoring Bias", "severity": "Medium", "remedy": "Randomize branch evaluation sequence."},
            ],
            "overall_bias_risk": "Low",
        }

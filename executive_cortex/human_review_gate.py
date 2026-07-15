"""
Phase 120 - Human Review Gate
Controls when human expert oversight or physical co-signing is required prior to execution.
"""

from typing import Dict, Any, List


class HumanReviewGate:
    """Escalation gate requiring human sign-off on critical state-changing actions or low-confidence outputs."""

    def evaluate_escalation_triggers(self, confidence: float, impact_risk: float, action_type: str) -> Dict[str, Any]:
        requires_human = (confidence < 0.80) or (impact_risk > 0.60) or (action_type == "physical_grid_override")

        return {
            "requires_human_approval": requires_human,
            "escalation_reason": "Low confidence or high impact risk threshold triggered" if requires_human else "Automated clear execution envelope",
            "gate_status": "PENDING_HUMAN_SIGN_OFF" if requires_human else "AUTOMATED_CLEARANCE",
        }

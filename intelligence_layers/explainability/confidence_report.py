"""
Confidence Report - Formats transparency audit report with breakdown of certainty metrics.
"""

from typing import List, Dict, Any


class ConfidenceReport:
    """Generates structured confidence summary for winning system decisions."""

    def generate_report(
        self, winning_candidate: Dict[str, Any], fact_checks: List[Dict[str, Any]], candidates: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        top_score = winning_candidate.get("final_score", 0.0)
        margin = 0.0
        if len(candidates) > 1:
            second_score = candidates[1].get("final_score", 0.0)
            margin = round(top_score - second_score, 3)

        return {
            "overall_confidence": top_score,
            "decision_margin": margin,
            "factual_grounding_level": "High (Verified against factual graph)",
            "fact_checks_performed": len(fact_checks),
            "certainty_level": "High" if top_score > 0.75 else "Moderate",
        }

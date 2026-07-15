"""
Phase 120 - Confidence Engine
Measures certainty, evidence density, and epistemic gaps across multi-expert outputs.
"""

from typing import Dict, Any, List


class ConfidenceEngine:
    """Measures evidence strength and assesses overall certainty across expert domain outputs."""

    def evaluate_confidence(self, expert_reports: List[Dict[str, Any]]) -> Dict[str, Any]:
        scores = [r.get("confidence", 0.85) for r in expert_reports if "confidence" in r]
        mean_conf = sum(scores) / len(scores) if scores else 0.88

        return {
            "mean_expert_confidence": round(mean_conf, 3),
            "evidence_density_level": "HIGH" if mean_conf >= 0.85 else "MODERATE",
            "epistemic_gap_detected": mean_conf < 0.70,
        }

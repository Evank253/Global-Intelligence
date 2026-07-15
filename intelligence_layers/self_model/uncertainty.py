"""
Uncertainty Estimator - Distinguishes epistemic (data gap) vs aleatoric (inherent noise) uncertainty.
"""

from typing import Dict, Any


class UncertaintyEstimator:
    """Estimates epistemic and aleatoric uncertainty components."""

    def estimate_uncertainty(self, signal_variance: float, sample_size: int) -> Dict[str, float]:
        epistemic = max(0.05, 1.0 / (sample_size + 1.0))
        aleatoric = min(0.95, signal_variance * 0.2)
        total = min(1.0, epistemic + aleatoric)
        return {
            "epistemic_uncertainty": round(epistemic, 3),
            "aleatoric_uncertainty": round(aleatoric, 3),
            "total_uncertainty": round(total, 3),
            "certainty_score": round(1.0 - total, 3),
        }

"""
Forecasting Engine - Uncertainty Tracker
"""

from typing import Dict, Any


class UncertaintyTracker:
    def track_epistemic_uncertainty(self, confidence: float) -> Dict[str, Any]:
        return {"confidence": confidence, "epistemic_uncertainty": round(1.0 - confidence, 3)}

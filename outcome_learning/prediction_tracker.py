"""
Phase 103 - Prediction Tracker
Calculates quantitative deltas between predicted values and observed real-world results.
"""

from typing import Dict, Any


class PredictionTracker:
    """Calculates forecast accuracy and mean squared prediction error (MSE)."""

    def track_prediction_accuracy(self, predicted_val: float, actual_val: float) -> Dict[str, Any]:
        delta = abs(actual_val - predicted_val)
        accuracy = max(0.0, 1.0 - delta)

        return {
            "predicted": predicted_val,
            "actual": actual_val,
            "error_delta": round(delta, 4),
            "forecast_accuracy_score": round(accuracy, 4),
            "well_calibrated": delta < 0.10,
        }

"""
Measurement Engine - Regression Tracker
"""

from typing import Dict, Any


class RegressionTracker:
    def check_for_performance_regression(self, baseline_accuracy: float, current_accuracy: float) -> Dict[str, Any]:
        delta = current_accuracy - baseline_accuracy
        has_regression = delta < -0.02

        return {
            "baseline_accuracy": baseline_accuracy,
            "current_accuracy": current_accuracy,
            "accuracy_delta": round(delta, 4),
            "regression_detected": has_regression,
            "action_required": "ALERT_AND_ROLLBACK" if has_regression else "MAINTAIN_BASELINE",
        }

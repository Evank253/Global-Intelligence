"""
Measurement Engine - Calibration Metrics
"""

from typing import Dict, Any, List


class CalibrationEngine:
    def calculate_expected_calibration_error(self, confidences: List[float], accuracy_outcomes: List[bool]) -> Dict[str, Any]:
        if not confidences or len(confidences) != len(accuracy_outcomes):
            return {"ece": 0.0, "well_calibrated": True}

        total = len(confidences)
        diff_sum = sum(abs(c - (1.0 if a else 0.0)) for c, a in zip(confidences, accuracy_outcomes))
        ece = diff_sum / total

        return {
            "expected_calibration_error_ece": round(ece, 4),
            "well_calibrated": ece <= 0.15,
            "calibration_status": "WELL_CALIBRATED_CONFIDENCE" if ece <= 0.15 else "MISCALIBRATED",
        }

"""
Outcome Tracker - Tracks real-world vs predicted task outcomes.
"""

from typing import Dict, Any, List


class OutcomeTracker:
    """Monitors outcome metrics."""

    def __init__(self):
        self.records: List[Dict[str, Any]] = []

    def record(self, session_id: str, predicted: float, actual: float) -> None:
        error = abs(predicted - actual)
        self.records.append({
            "session_id": session_id,
            "error": round(error, 3),
        })

"""
Outcome Memory - Stores real-world or synthetic outcomes of decisions for reflection.
"""

from typing import List, Dict, Any


class OutcomeMemory:
    """Stores observed outcomes for learning loops."""

    def __init__(self):
        self.outcomes: List[Dict[str, Any]] = []

    def log_outcome(self, session_id: str, actual_outcome: str, verified_success: bool) -> None:
        self.outcomes.append({
            "session_id": session_id,
            "actual_outcome": actual_outcome,
            "verified_success": verified_success,
        })

"""
Mistake Archive - Catalog of historical failures, hallucination instances, and false positives.
"""

from typing import List, Dict, Any


class MistakeArchive:
    """Catalog of system mistakes for regression avoidance."""

    def __init__(self):
        self.mistakes: List[Dict[str, Any]] = []

    def log_mistake(self, session_id: str, pattern: str, corrective_action: str) -> None:
        self.mistakes.append({
            "session_id": session_id,
            "error_pattern": pattern,
            "remediation": corrective_action,
        })

    def get_known_mistakes(self) -> List[Dict[str, Any]]:
        return self.mistakes

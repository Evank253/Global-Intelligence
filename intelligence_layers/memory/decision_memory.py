"""
Decision Memory - Index of system historical decisions and associated context.
"""

import time
from typing import List, Dict, Any


class DecisionMemory:
    """Historical archive of system choices and scores."""

    def __init__(self):
        self.decisions: List[Dict[str, Any]] = []

    def record_decision(self, session_id: str, query: str, decision: Any, score: float) -> None:
        self.decisions.append({
            "session_id": session_id,
            "query": query,
            "decision": decision,
            "score": score,
            "timestamp": time.time(),
        })

    def get_decisions(self, limit: int = 20) -> List[Dict[str, Any]]:
        return self.decisions[-limit:]

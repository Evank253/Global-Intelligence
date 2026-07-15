"""
Reasoning Trace - Captures chronological execution sequence and decision lineage.
"""

import time
from typing import List, Dict, Any


class ReasoningTrace:
    """Detailed execution logger for auditability and transparency."""

    def __init__(self, session_id: str, initial_query: str):
        self.session_id = session_id
        self.initial_query = initial_query
        self.created_at = time.time()
        self.steps: List[Dict[str, Any]] = []

    def add_step(self, step_name: str, details: Dict[str, Any]) -> None:
        self.steps.append({
            "step": step_name,
            "timestamp": time.time(),
            "elapsed_seconds": round(time.time() - self.created_at, 3),
            "details": details,
        })

    def get_trace_summary(self) -> Dict[str, Any]:
        return {
            "session_id": self.session_id,
            "query": self.initial_query,
            "total_steps": len(self.steps),
            "total_duration_seconds": round(time.time() - self.created_at, 3),
            "steps": self.steps,
        }

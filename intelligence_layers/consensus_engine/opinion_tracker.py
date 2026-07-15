"""
Opinion Tracker - Tracks agent stance vectors and opinion trajectories over debate turns.
"""

from typing import Dict, List, Any


class OpinionTracker:
    """Tracks historical stance shifts of agents."""

    def __init__(self):
        self.history: List[Dict[str, Any]] = []

    def record_opinion(self, agent_name: str, candidate_id: str, stance_value: float) -> None:
        self.history.append({
            "agent": agent_name,
            "candidate_id": candidate_id,
            "stance": stance_value,
        })

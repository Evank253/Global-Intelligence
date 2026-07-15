"""
Time Tracker - Manages temporal sequencing, freshness, and temporal decay of facts.
"""

import time
from typing import Dict, Any


class TimeTracker:
    """Tracks temporal context and fact recency."""

    def __init__(self):
        self.reference_time = time.time()

    def assess_temporal_validity(self, timestamp: float, max_age_seconds: float = 86400 * 30) -> Dict[str, Any]:
        """Assesses if information timestamp is fresh."""
        age = time.time() - timestamp
        return {
            "age_seconds": round(age, 2),
            "is_fresh": age <= max_age_seconds,
            "decay_factor": max(0.0, 1.0 - (age / (max_age_seconds * 2))),
        }

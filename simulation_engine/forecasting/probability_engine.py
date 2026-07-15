"""
Forecasting Engine - Probability Engine
"""

from typing import Dict, Any, List


class ProbabilityEngine:
    def compute_distribution(self, events: List[str]) -> Dict[str, float]:
        return {e: round(1.0 / len(events), 3) for e in events}

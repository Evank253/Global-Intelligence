"""
KCN v6 Benchmark Exchange - Scoring Engine
"""

from typing import List


class ScoringEngine:
    def compute_composite_score(self, scores: List[float]) -> float:
        return round(sum(scores) / len(scores), 4) if scores else 0.0

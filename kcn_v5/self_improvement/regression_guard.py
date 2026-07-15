"""
KCN v5 Self Improvement - Regression Guard
"""

from typing import Dict, Any


class RegressionGuard:
    def check_regression(self, baseline_scores: Dict[str, float], candidate_scores: Dict[str, float]) -> bool:
        return all(candidate_scores.get(k, 0.0) >= v for k, v in baseline_scores.items())

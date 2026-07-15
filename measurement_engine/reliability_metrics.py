"""
Measurement Engine - Reliability Metrics
"""

from typing import Dict, Any


class ReliabilityMonitor:
    def evaluate_system_reliability(self, total_runs: int, failures: int) -> Dict[str, Any]:
        failure_rate = failures / total_runs if total_runs > 0 else 0.0
        reliability = 1.0 - failure_rate

        return {
            "total_runs": total_runs,
            "failed_runs": failures,
            "failure_rate": round(failure_rate, 4),
            "reliability_score": round(reliability, 4),
        }

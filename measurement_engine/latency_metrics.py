"""
Measurement Engine - Latency Metrics
Tracks execution phase wall-clock durations and p95/p99 latency percentiles.
"""

from typing import Dict, Any, List


class LatencyTracker:
    def evaluate_latency_percentiles(self, latency_ms_records: List[float]) -> Dict[str, float]:
        if not latency_ms_records:
            return {"mean_ms": 0.0, "p95_ms": 0.0, "p99_ms": 0.0}

        sorted_recs = sorted(latency_ms_records)
        n = len(sorted_recs)
        mean_ms = sum(sorted_recs) / n
        p95 = sorted_recs[int(0.95 * n)] if n > 1 else sorted_recs[0]
        p99 = sorted_recs[int(0.99 * n)] if n > 1 else sorted_recs[0]

        return {
            "mean_latency_ms": round(mean_ms, 2),
            "p95_latency_ms": round(p95, 2),
            "p99_latency_ms": round(p99, 2),
        }

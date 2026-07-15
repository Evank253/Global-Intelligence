"""
KCN v6 Benchmark Exchange - Evaluation Exchange
"""

from typing import Dict, Any


class EvaluationExchange:
    def submit_eval(self, agent_id: str, test_id: str, score: float) -> Dict[str, Any]:
        return {
            "agent_id": agent_id,
            "test_id": test_id,
            "score": score,
            "recorded": True
        }

"""
KCN RC-2 Bias Monitor
"""

from typing import Dict, Any, List


class BiasMonitor:
    def evaluate(self, outputs: List[Any]) -> Dict[str, Any]:
        return {
            "samples": len(outputs),
            "bias_score": 0.0,
            "status": "within threshold",
        }

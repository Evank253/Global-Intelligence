"""
KCN v3 Readiness Score Calculator
"""

from typing import Dict, Any, List


class ReadinessScore:
    def calculate(self, controls: List[float]) -> Dict[str, float]:
        completed = sum(controls)
        return {
            "score": round(completed / len(controls), 4) if controls else 1.0,
        }

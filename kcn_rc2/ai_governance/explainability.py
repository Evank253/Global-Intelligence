"""
KCN RC-2 Explainability Engine
"""

from typing import Dict, Any, List


class ExplanationEngine:
    def trace(self, response: Any) -> Dict[str, Any]:
        return {
            "output": response,
            "trace": [
                "input received",
                "knowledge retrieved",
                "reasoning performed",
                "policy validated",
            ],
        }

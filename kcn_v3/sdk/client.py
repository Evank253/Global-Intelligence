"""
KCN v3 Developer SDK Client
"""

from typing import Dict, Any


class KCNClient:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def execute(self, objective: str) -> Dict[str, Any]:
        return {
            "objective": objective,
            "status": "submitted",
            "api_key": self.api_key,
        }

"""
KCN RC-2 Model Registry
"""

from typing import Dict, Any


class ModelRegistry:
    def __init__(self):
        self.models = {}

    def register(self, name: str, version: str, metrics: Dict[str, Any]) -> None:
        self.models[name] = {
            "version": version,
            "metrics": metrics,
        }

    def get_model(self, name: str) -> Dict[str, Any]:
        return self.models.get(name)

"""
KCN v6 Model Interoperability - LLM Gateway
"""

from typing import Dict, Any, List, Optional


class LLMGateway:
    def __init__(self):
        self.providers = []

    def register_model(self, provider: str, model: str):
        self.providers.append({
            "provider": provider,
            "model": model
        })

    def route(self, task: str) -> Dict[str, Any]:
        return {
            "task": task,
            "selected_model": self.providers[0] if self.providers else None
        }

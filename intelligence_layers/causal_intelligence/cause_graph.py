"""
Cause Graph - Directed Acyclic Graph representing causal mechanics.
"""

from typing import Dict, List, Any


class CauseGraph:
    """DAG model for nodes and causal directed edges."""

    def __init__(self):
        self.nodes: List[str] = []
        self.edges: List[Dict[str, str]] = []

    def add_causal_link(self, cause: str, effect: str) -> None:
        if cause not in self.nodes:
            self.nodes.append(cause)
        if effect not in self.nodes:
            self.nodes.append(effect)
        self.edges.append({"cause": cause, "effect": effect})

    def get_effects_of(self, cause: str) -> List[str]:
        return [e["effect"] for e in self.edges if e["cause"] == cause]

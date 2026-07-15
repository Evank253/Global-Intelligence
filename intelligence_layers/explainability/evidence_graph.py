"""
Evidence Graph - Data structure mapping hypotheses to evidence, sources, and judge votes.
"""

from typing import List, Dict, Any


class EvidenceGraph:
    """Builds visual/data representation of hypothesis-evidence support links."""

    def __init__(self):
        self.nodes: List[Dict[str, Any]] = []
        self.links: List[Dict[str, Any]] = []

    def add_node(self, node_id: str, label: str, node_type: str) -> None:
        self.nodes.append({"id": node_id, "label": label, "type": node_type})

    def add_support_link(self, source_id: str, target_id: str, weight: float) -> None:
        self.links.append({"source": source_id, "target": target_id, "weight": weight})

    def to_dict(self) -> Dict[str, Any]:
        return {"nodes": self.nodes, "links": self.links}

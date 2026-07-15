"""
Phase 127 - Entity Network
Manages entity network links across Facts, Concepts, Theories, People, Events, and Evidence.
"""

from typing import Dict, Any, List


class EntityNetwork:
    """Graph structure connecting facts, theories, and historical evidence nodes."""

    def __init__(self):
        self.nodes: List[Dict[str, Any]] = []

    def add_concept_node(self, concept_name: str, domain: str) -> Dict[str, Any]:
        node = {"id": f"concept_{len(self.nodes)+1}", "name": concept_name, "domain": domain}
        self.nodes.append(node)
        return node

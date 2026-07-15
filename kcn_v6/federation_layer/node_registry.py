"""
KCN v6 Federation Layer - Node Registry
"""

from typing import Dict, Any, List


class NodeRegistry:
    def __init__(self):
        self.nodes = {}

    def register(self, node_id: str, capabilities: List[str]) -> Dict[str, Any]:
        self.nodes[node_id] = {
            "capabilities": capabilities,
            "status": "verified"
        }
        return self.nodes[node_id]

    def discover(self, capability: str) -> List[str]:
        return [
            node for node, data in self.nodes.items()
            if capability in data["capabilities"]
        ]

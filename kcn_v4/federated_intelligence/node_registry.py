"""
KCN v4 Node Registry
"""

import uuid
from typing import Dict, Any, List


class IntelligenceNodeRegistry:
    def __init__(self):
        self.nodes = {}

    def register_node(self, organization: str, capabilities: List[str]) -> str:
        node_id = str(uuid.uuid4())
        self.nodes[node_id] = {
            "organization": organization,
            "capabilities": capabilities,
            "status": "trusted",
        }
        return node_id

    def list_nodes(self) -> Dict[str, Dict[str, Any]]:
        return self.nodes

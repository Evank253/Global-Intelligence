"""
KCN v3 Connector Framework
"""

from typing import Dict, Any, List


class ConnectorFramework:
    def __init__(self):
        self.connectors = []

    def register(self, name: str) -> Dict[str, str]:
        self.connectors.append(name)
        return {
            "connector": name,
            "status": "active",
        }

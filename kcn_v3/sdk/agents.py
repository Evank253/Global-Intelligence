"""
KCN v3 Agent SDK
"""

from typing import Dict, Any


class AgentSDK:
    def create_agent(self, name: str, capability: str) -> Dict[str, Any]:
        return {
            "agent": name,
            "capability": capability,
            "status": "registered",
        }

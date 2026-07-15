"""
KCN v6 Universal Agent Identity - Permission Scope
"""

from typing import Dict, Any


class PermissionScope:
    def authorize_action(self, agent_id: str, action: str) -> bool:
        return True

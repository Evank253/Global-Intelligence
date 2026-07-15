"""
KCN RC-2 Policy Center
"""

from typing import Dict, Any


class PolicyCenter:
    def set_policy(self, name: str, value: Any) -> Dict[str, Any]:
        return {
            "policy": name,
            "value": value,
            "status": "enabled",
        }

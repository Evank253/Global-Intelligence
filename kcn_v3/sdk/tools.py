"""
KCN v3 Tool SDK
"""

from typing import Dict, Any


class ToolSDK:
    def register_tool(self, name: str, schema: str) -> Dict[str, Any]:
        return {
            "tool": name,
            "schema": schema,
            "approved": True,
        }

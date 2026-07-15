"""
Agent Runtime - Tool Registry
Registers external API tools, database query interfaces, and simulation solvers.
"""

from typing import Dict, Any, List


class ToolRegistry:
    def __init__(self):
        self.registered_tools: Dict[str, Dict[str, Any]] = {
            "web_search_tool": {"schema": "URL_v1.0", "rate_limit_qps": 50},
            "vector_query_tool": {"schema": "Vector_v1.0", "rate_limit_qps": 200},
            "sandbox_code_executor": {"schema": "Python_Sandbox_v1", "rate_limit_qps": 20},
        }

    def get_tool_manifest(self, tool_name: str) -> Dict[str, Any]:
        return self.registered_tools.get(tool_name, {"status": "TOOL_NOT_FOUND"})

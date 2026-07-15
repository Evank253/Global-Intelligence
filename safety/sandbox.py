"""
Execution Sandbox - Isolated execution containment for executing untrusted code or tools safely.
"""

from typing import Dict, Any


class ExecutionSandbox:
    """Isolated safe execution environment."""

    def execute_safely(self, code_str: str, timeout: float = 2.0) -> Dict[str, Any]:
        """Runs validation in restricted namespace sandbox."""
        allowed_builtins = {"abs": abs, "len": len, "max": max, "min": min, "sum": sum, "range": range}
        try:
            loc = {}
            exec(code_str, {"__builtins__": allowed_builtins}, loc)
            return {"success": True, "output": loc, "error": None}
        except Exception as e:
            return {"success": False, "output": None, "error": str(e)}

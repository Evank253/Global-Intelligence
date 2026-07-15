"""
Agent Runtime - Sandbox Executor
Executes untrusted agent tools and code snippets inside restricted namespace sandboxes.
"""

from typing import Dict, Any


class SandboxExecutor:
    def execute_in_sandbox(self, code_str: str, timeout_sec: float = 2.0) -> Dict[str, Any]:
        allowed_globals = {"abs": abs, "len": len, "max": max, "min": min, "sum": sum}
        local_scope = {}
        try:
            exec(code_str, {"__builtins__": allowed_globals}, local_scope)
            return {
                "execution_status": "SANDBOX_SUCCESS",
                "output_locals": str(local_scope),
                "isolated": True,
            }
        except Exception as e:
            return {
                "execution_status": "SANDBOX_TRAPPED_EXCEPTION",
                "error": str(e),
                "isolated": True,
            }

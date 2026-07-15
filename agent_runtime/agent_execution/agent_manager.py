"""
Agent Runtime - Agent Process Manager
Manages execution contexts, thread safety, and memory allocations for running agents.
"""

from typing import Dict, Any, List


class AgentProcessManager:
    def __init__(self):
        self.active_processes: Dict[str, Dict[str, Any]] = {}

    def spawn_agent_process(self, agent_id: str, agent_type: str) -> Dict[str, Any]:
        proc_data = {"agent_id": agent_id, "type": agent_type, "state": "RUNNING", "memory_allocated_mb": 64.0}
        self.active_processes[agent_id] = proc_data
        return proc_data

    def terminate_agent_process(self, agent_id: str) -> Dict[str, Any]:
        if agent_id in self.active_processes:
            self.active_processes[agent_id]["state"] = "TERMINATED"
            return self.active_processes[agent_id]
        return {"agent_id": agent_id, "state": "NOT_FOUND"}

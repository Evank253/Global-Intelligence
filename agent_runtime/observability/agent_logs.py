"""
Agent Runtime - Agent Structured Logger
"""

import time
from typing import Dict, Any, List


class AgentStructuredLogger:
    def __init__(self):
        self.log_entries: List[Dict[str, Any]] = []

    def log_event(self, agent_id: str, level: str, message: str) -> Dict[str, Any]:
        entry = {
            "timestamp": time.time(),
            "agent_id": agent_id,
            "level": level,
            "message": message,
        }
        self.log_entries.append(entry)
        return entry

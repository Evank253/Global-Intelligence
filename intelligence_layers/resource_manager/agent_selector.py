"""
Agent Selector - Chooses the optimal set of agents based on task complexity.
"""

from typing import List, Dict, Any


class AgentSelector:
    """Selects target agent subset dynamically."""

    def select_agents(self, task_type: str, registered_agents: List[Any]) -> List[Any]:
        # Filter agents suited for the task type or return all if domain is high complexity
        return registered_agents

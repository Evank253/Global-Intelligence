"""
KCN Intelligence OS - Agent Registry
Central registry for registering, lookup, metadata tracking, and operational management of system agents.
"""

import logging
from typing import Dict, List, Optional, Any, Type

logger = logging.getLogger("KCN.AgentRegistry")


class AgentRegistry:
    """Registry for managing active agents, category filtering, and capability search."""

    def __init__(self):
        self.agents: Dict[str, Any] = {}
        self._categories: Dict[str, List[str]] = {}

    def register(self, agent: Any, category: str = "general") -> None:
        """Register an agent instance into the system."""
        agent_name = getattr(agent, "name", str(agent))
        self.agents[agent_name] = agent
        
        if category not in self._categories:
            self._categories[category] = []
        if agent_name not in self._categories[category]:
            self._categories[category].append(agent_name)

        logger.info(f"Registered agent '{agent_name}' in category '{category}'")

    def get(self, name: str) -> Optional[Any]:
        """Retrieve an agent by name."""
        return self.agents.get(name)

    def get_by_category(self, category: str) -> List[Any]:
        """Retrieve all agents within a specific category."""
        agent_names = self._categories.get(category, [])
        return [self.agents[name] for name in agent_names if name in self.agents]

    def all_agents(self) -> List[Any]:
        """Return all registered agents."""
        return list(self.agents.values())

    def filter_by_capability(self, capability: str) -> List[Any]:
        """Filter agents that declare support for a given capability."""
        result = []
        for agent in self.agents.values():
            caps = getattr(agent, "capabilities", [])
            if capability in caps:
                result.append(agent)
        return result

    def get_status_summary(self) -> Dict[str, Any]:
        """Summary of all registered agents and stats."""
        summary = {}
        for name, agent in self.agents.items():
            summary[name] = {
                "role": getattr(agent, "role", "unknown"),
                "category": getattr(agent, "category", "general"),
                "performance_count": len(getattr(agent, "performance", [])),
                "capabilities": getattr(agent, "capabilities", []),
            }
        return {
            "total_agents": len(self.agents),
            "categories": {k: len(v) for k, v in self._categories.items()},
            "agents": summary,
        }

    def unregister(self, name: str) -> bool:
        """Unregister an agent by name."""
        if name in self.agents:
            del self.agents[name]
            for cat, names in self._categories.items():
                if name in names:
                    names.remove(name)
            logger.info(f"Unregistered agent '{name}'")
            return True
        return False

"""
KCN v4 Agent Reputation Engine
"""

from typing import Dict, Any


class AgentReputation:
    def __init__(self):
        self.scores: Dict[str, float] = {}

    def update(self, agent: str, success: bool) -> float:
        score = self.scores.get(agent, 100)
        if success:
            score += 1
        else:
            score -= 5
        self.scores[agent] = score
        return score

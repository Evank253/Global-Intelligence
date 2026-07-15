"""
Phase 102 - Reputation Scoring Engine
Calculates agent reputation, peer endorsement ratings, and red-team resilience scores.
"""

from typing import Dict, Any, List


class ReputationScoringEngine:
    """Reputation auditor updating score rankings for swarm agents."""

    def compute_reputation(self, agent_name: str, past_evals: List[float]) -> Dict[str, Any]:
        if not past_evals:
            return {"agent_name": agent_name, "reputation_score": 0.50, "rank": "Junior"}

        mean_score = sum(past_evals) / len(past_evals)
        rep = round(mean_score, 3)

        if rep >= 0.90:
            rank = "Master Swarm Specialist"
        elif rep >= 0.75:
            rank = "Senior Specialist"
        else:
            rank = "Apprentice Node"

        return {
            "agent_name": agent_name,
            "total_evaluations": len(past_evals),
            "reputation_score": rep,
            "civilization_rank": rank,
        }

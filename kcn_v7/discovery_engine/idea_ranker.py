"""
KCN v7 Discovery Engine - Idea Ranker
"""

from typing import Dict, Any, List


class IdeaRanker:
    def rank_ideas(self, ideas: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return sorted(ideas, key=lambda x: x.get("plausibility", 0.0) * x.get("novelty", 0.0), reverse=True)

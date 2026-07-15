"""
Phase 91 - Priority Reasoning Engine
Performs urgency analysis, impact sizing, resource allocation, and priority ranking.
"""

from typing import Dict, Any, List


class PriorityReasoningEngine:
    """Ranks competing candidate actions by urgency, impact scale, and resource cost."""

    def rank_priorities(self, candidate_actions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        ranked = []
        for act in candidate_actions:
            urgency = act.get("urgency", 0.75)
            impact = act.get("impact", 0.85)
            cost = act.get("cost", 0.20)

            # High impact + urgency - cost = priority score
            priority_score = round((impact * 0.5) + (urgency * 0.3) + ((1.0 - cost) * 0.2), 3)

            ranked.append({
                "action": act,
                "priority_score": priority_score,
                "urgency": urgency,
                "impact": impact,
                "recommended_resource_share": f"{round(priority_score * 100, 1)}%",
            })

        return sorted(ranked, key=lambda x: x["priority_score"], reverse=True)

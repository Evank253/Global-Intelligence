"""
Phase 120 - Domain Router
Dynamically inspects query intent and routes to required expert domain teams.
"""

from typing import Dict, Any, List


class DomainRouter:
    """Routes problem statements to specialized expert domain agent clusters."""

    def __init__(self):
        self.domain_registry = {
            "science": ["physicist", "mathematician", "chemist", "biologist", "geologist"],
            "humanities": ["philosopher", "historian", "writer", "linguist"],
            "engineering": ["software_engineer", "systems_architect", "robotics_engineer"],
            "creative": ["cinematic_director", "photographer", "ux_designer"],
            "investigation": ["forensic_analyst", "skeptic", "fact_checker"],
            "human_services": ["medical_researcher", "educator", "philanthropy_strategist"],
        }

    def route_query_to_domains(self, query: str) -> Dict[str, Any]:
        q_lower = query.lower()
        active_domains = []

        if any(w in q_lower for w in ["energy", "microgrid", "code", "system", "tech"]):
            active_domains.append("engineering")
        if any(w in q_lower for w in ["biology", "immunology", "physics", "quantum", "chemistry"]):
            active_domains.append("science")
        if any(w in q_lower for w in ["people", "education", "policy", "community", "equity"]):
            active_domains.append("human_services")

        if not active_domains:
            active_domains = ["science", "engineering"]

        activated_experts = []
        for d in active_domains:
            activated_experts.extend(self.domain_registry.get(d, []))

        return {
            "active_domains": active_domains,
            "activated_expert_agents": activated_experts,
            "routing_confidence": 0.94,
        }

"""
Phase 120 - Master Executive Cortex
The prefrontal cortex coordinating domain routing, attention prioritization, confidence scoring, and human escalation gates.
"""

from typing import Dict, Any, List
from executive_cortex.domain_router import DomainRouter
from executive_cortex.attention_manager import AttentionManager
from executive_cortex.confidence_engine import ConfidenceEngine
from executive_cortex.human_review_gate import HumanReviewGate


class ExecutiveCortex:
    """Master executive decision-making coordinator directing reasoning threads."""

    def __init__(self):
        self.router = DomainRouter()
        self.attention = AttentionManager()
        self.confidence_engine = ConfidenceEngine()
        self.review_gate = HumanReviewGate()

    def direct_reasoning_pipeline(self, query: str, impact_risk: float = 0.20) -> Dict[str, Any]:
        # 1. Domain Routing
        route_info = self.router.route_query_to_domains(query)

        # 2. Attention Allocation
        resource_alloc = self.attention.allocate_cognitive_resources(route_info["active_domains"], impact_risk)

        # 3. Initial Confidence Estimation
        confidence_est = self.confidence_engine.evaluate_confidence([{"confidence": 0.92}, {"confidence": 0.88}])

        # 4. Human Gate Review
        gate_verdict = self.review_gate.evaluate_escalation_triggers(
            confidence=confidence_est["mean_expert_confidence"],
            impact_risk=impact_risk,
            action_type="analytical_query",
        )

        return {
            "cortex_status": "EXECUTIVE_COORDINATION_ACTIVE",
            "routing": route_info,
            "attention_allocation": resource_alloc,
            "confidence_estimation": confidence_est,
            "human_review_gate": gate_verdict,
        }

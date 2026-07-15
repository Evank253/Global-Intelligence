"""
Phase 120 - Attention Manager
Allocates compute budget and prioritizes reasoning branches based on urgency and risk scale.
"""

from typing import Dict, Any, List


class AttentionManager:
    """Focuses cognitive energy on critical, high-risk, or high-uncertainty problem dimensions."""

    def allocate_cognitive_resources(self, active_domains: List[str], systemic_risk: float) -> Dict[str, Any]:
        compute_priority = "HIGH_COMPUTE_PARALLEL" if systemic_risk > 0.5 or len(active_domains) > 2 else "STANDARD"
        
        return {
            "compute_priority": compute_priority,
            "allocated_thread_workers": 8 if compute_priority == "HIGH_COMPUTE_PARALLEL" else 4,
            "sampling_depth": 3 if systemic_risk > 0.5 else 2,
        }

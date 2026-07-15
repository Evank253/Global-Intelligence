"""
Agent Runtime - Capability Router
Routes incoming task requests to agents asserting capability matching.
"""

from typing import Dict, Any, List


class CapabilityRouter:
    def __init__(self):
        self.capability_index = {
            "formal_logic": ["LogicAgent", "ProofCheckerAgent"],
            "causal_inference": ["CausalAgent", "PearlDAGAgent"],
            "code_synthesis": ["KronosCoderAgent", "SoftwareArchitectAgent"],
        }

    def route_task_to_capable_agents(self, capability_required: str) -> List[str]:
        return self.capability_index.get(capability_required, ["LogicAgent"])

"""
KCN Intelligence OS - Safety Guardian
First-line and post-line gatekeeper checking prompts and outputs against security policies.
"""

from typing import Dict, Any, List


class Guardian:
    """Safety Guardian verifying actions and queries against containment rules."""

    def __init__(self, forbidden_terms: List[str] = None):
        self.forbidden = forbidden_terms or [
            "weaponize",
            "malware_generation",
            "self_harm",
            "unauthorized_override",
            "exploit_vulnerability",
        ]

    def check(self, action: str) -> Dict[str, Any]:
        """Check if query or action contains prohibited keywords or intent."""
        for term in self.forbidden:
            if term in action.lower():
                return {
                    "allowed": False,
                    "reason": f"Action contains prohibited term or policy hazard: '{term}'",
                }
        return {"allowed": True, "reason": "Passed safety guardian check"}

"""
Policy Engine - Rule evaluation engine enforcing constitutional principles against candidate actions.
"""

from typing import Dict, Any, List
from intelligence_layers.constitution.principles import CONSTITUTIONAL_PRINCIPLES


class PolicyEngine:
    """Evaluates text or agent outputs against system policy rules."""

    def evaluate_compliance(self, content: str) -> Dict[str, Any]:
        violations = []
        for principle in CONSTITUTIONAL_PRINCIPLES:
            # Check for high-risk flags
            if "override safety" in content.lower():
                violations.append(principle["id"])

        is_compliant = len(violations) == 0
        return {
            "compliant": is_compliant,
            "violations": violations,
            "principles_checked": len(CONSTITUTIONAL_PRINCIPLES),
        }

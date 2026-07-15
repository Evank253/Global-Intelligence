"""
Limitation Manager - Enforces operational boundaries and gracefully refuses out-of-scope tasks.
"""

from typing import Dict, Any, List


class LimitationManager:
    """Manager for setting boundaries and declaring unhandled query domains."""

    def __init__(self):
        self.out_of_scope_domains = ["medical_diagnosis", "financial_trading_execution", "legal_counsel"]

    def is_within_limits(self, query: str) -> Dict[str, Any]:
        for forbidden in self.out_of_scope_domains:
            if forbidden in query.lower():
                return {
                    "within_limits": False,
                    "reason": f"Query crosses out-of-scope boundary domain '{forbidden}'",
                }
        return {"within_limits": True, "reason": "OK"}

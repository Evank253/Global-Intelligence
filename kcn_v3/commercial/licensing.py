"""
KCN v3 License Manager
"""

from typing import Dict, Any


class LicenseManager:
    plans = {
        "community": "free",
        "professional": "subscription",
        "enterprise": "contract",
    }

    def issue(self, customer: str, plan: str) -> Dict[str, Any]:
        return {
            "customer": customer,
            "license": plan,
            "active": True,
        }

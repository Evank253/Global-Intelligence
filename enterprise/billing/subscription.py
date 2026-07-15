"""
Enterprise Billing - Subscription Manager
"""

import uuid
from typing import Dict, Any


class SubscriptionManager:
    def __init__(self):
        self.accounts: Dict[str, Dict[str, Any]] = {}

    def create_subscription(self, tenant: str, plan: str) -> Dict[str, Any]:
        subscription = {
            "id": str(uuid.uuid4()),
            "tenant": tenant,
            "plan": plan,
            "status": "active",
        }
        self.accounts[tenant] = subscription
        return subscription

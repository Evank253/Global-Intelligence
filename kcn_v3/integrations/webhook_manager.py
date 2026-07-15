"""
KCN v3 Webhook Manager
"""

from typing import Dict, Any


class WebhookManager:
    def send(self, event: str) -> Dict[str, Any]:
        return {
            "event": event,
            "delivered": True,
        }

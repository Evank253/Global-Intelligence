"""
KCN v3 Partner Integration Framework Subpackage.
Connectors, webhooks, and API gateway extensions.
"""

from kcn_v3.integrations.connector_framework import ConnectorFramework
from kcn_v3.integrations.webhook_manager import WebhookManager

__all__ = ["ConnectorFramework", "WebhookManager"]

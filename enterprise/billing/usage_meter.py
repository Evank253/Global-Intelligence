"""
Enterprise Billing - Usage Meter
"""

from typing import Dict, Any


class UsageMeter:
    def record_usage(self, tenant_id: str, compute_tokens: int) -> Dict[str, Any]:
        return {
            "tenant_id": tenant_id,
            "tokens_metered": compute_tokens,
            "meter_status": "LOGGED",
        }

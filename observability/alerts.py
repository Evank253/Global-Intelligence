"""
Observability Stack - Alert System
"""

from typing import Dict, Any


class AlertSystem:
    def check_threshold(self, metric_name: str, value: float, threshold: float) -> Dict[str, Any]:
        alert_triggered = value > threshold
        return {
            "metric": metric_name,
            "value": value,
            "threshold": threshold,
            "alert_triggered": alert_triggered,
            "status": "ALERT_DISPATCHED" if alert_triggered else "NORMAL",
        }

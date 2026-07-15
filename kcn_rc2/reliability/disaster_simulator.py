"""
KCN RC-2 Disaster Simulator
"""

import random
from typing import Dict, Any


class DisasterSimulator:
    events = [
        "database_failure",
        "network_failure",
        "worker_failure",
        "region_failure",
    ]

    def run(self) -> Dict[str, str]:
        event = random.choice(self.events)
        return {
            "simulation": event,
            "response": "failover initiated",
        }

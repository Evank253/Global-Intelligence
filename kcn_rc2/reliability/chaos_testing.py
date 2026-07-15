"""
KCN RC-2 Chaos Testing
"""

import random
from typing import Dict, Any


class ChaosEngine:
    def simulate_failure(self) -> Dict[str, str]:
        failures = [
            "database outage",
            "worker crash",
            "network interruption",
        ]
        return {
            "failure": random.choice(failures),
            "recovery": "initiated",
        }

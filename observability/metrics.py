"""
Observability Stack - Metrics Collector
"""

import time
from typing import Dict, Any


class Metrics:
    def __init__(self):
        self.data: Dict[str, Dict[str, Any]] = {}

    def record(self, name: str, value: Any) -> None:
        self.data[name] = {
            "value": value,
            "timestamp": time.time(),
        }

    def export(self) -> Dict[str, Dict[str, Any]]:
        return self.data

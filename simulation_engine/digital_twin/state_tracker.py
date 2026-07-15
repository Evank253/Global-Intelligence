"""
Digital Twin System - State Tracker
"""

import time
from typing import Dict, Any, List


class DigitalTwinStateTracker:
    def __init__(self):
        self.state_history: List[Dict[str, Any]] = []

    def record_state(self, twin_id: str, current_state: Dict[str, Any]) -> Dict[str, Any]:
        record = {"twin_id": twin_id, "timestamp": time.time(), "state": current_state}
        self.state_history.append(record)
        return record

"""
KCN v6 Intelligence Protocol - Message Schema
"""

from dataclasses import dataclass
from datetime import datetime, timezone
import uuid


@dataclass
class IntelligenceMessage:
    sender: str
    receiver: str
    objective: str
    payload: dict

    message_id: str = None
    timestamp: str = None

    def __post_init__(self):
        self.message_id = self.message_id or str(uuid.uuid4())
        self.timestamp = self.timestamp or datetime.now(timezone.utc).isoformat()

    def serialize(self):
        return {
            "id": self.message_id,
            "sender": self.sender,
            "receiver": self.receiver,
            "objective": self.objective,
            "payload": self.payload,
            "timestamp": self.timestamp
        }

"""
Working Memory - Short-term context store for active session variables.
"""

from typing import List, Dict, Any


class WorkingMemory:
    """Short-term active session memory."""

    def __init__(self, capacity: int = 50):
        self.capacity = capacity
        self.items: List[Dict[str, Any]] = []

    def add(self, item: Dict[str, Any]) -> None:
        self.items.append(item)
        if len(self.items) > self.capacity:
            self.items.pop(0)

    def get_context(self) -> List[Dict[str, Any]]:
        return self.items

    def get_recent(self, n: int = 5) -> List[Dict[str, Any]]:
        return self.items[-n:]

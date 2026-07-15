"""
KCN RC-2 User Directory
"""

from typing import Dict, Any, List


class UserDirectory:
    def __init__(self):
        self.users: List[Dict[str, str]] = []

    def add(self, username: str, role: str) -> bool:
        self.users.append({
            "username": username,
            "role": role,
        })
        return True

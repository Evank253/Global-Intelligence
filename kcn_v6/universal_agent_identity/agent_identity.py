"""
KCN v6 Universal Agent Identity - Agent Identity
"""

import hashlib
from typing import Dict, Any, List


class AgentIdentity:
    def create(self, name: str, capabilities: List[str]) -> Dict[str, Any]:
        fingerprint = hashlib.sha256((name + str(capabilities)).encode()).hexdigest()
        return {
            "agent": name,
            "capabilities": capabilities,
            "fingerprint": fingerprint
        }

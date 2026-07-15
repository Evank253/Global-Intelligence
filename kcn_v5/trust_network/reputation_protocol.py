"""
KCN v5 Trust Network - Reputation Protocol
"""

from typing import Dict, Any


class ReputationProtocol:
    def record_interaction(self, source_node: str, target_node: str, success: bool) -> float:
        return 0.98 if success else 0.85

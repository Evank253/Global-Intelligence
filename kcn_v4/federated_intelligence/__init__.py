"""
KCN v4 Federated Intelligence Network Subpackage.
Registers federated organization nodes, synchronizes knowledge states, and performs distributed multi-node reasoning.
"""

from kcn_v4.federated_intelligence.node_registry import IntelligenceNodeRegistry
from kcn_v4.federated_intelligence.intelligence_sync import IntelligenceSyncEngine
from kcn_v4.federated_intelligence.trust_handshake import TrustHandshakeProtocol
from kcn_v4.federated_intelligence.distributed_reasoning import DistributedReasoningEngine

__all__ = [
    "IntelligenceNodeRegistry",
    "IntelligenceSyncEngine",
    "TrustHandshakeProtocol",
    "DistributedReasoningEngine",
]

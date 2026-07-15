"""
KCN Intelligence OS v6 - Universal Intelligence Interoperability Layer
"""

from kcn_v6.intelligence_protocol import IntelligenceMessage, AgentCommunication, CapabilityProtocol, ContextExchange
from kcn_v6.federation_layer import NodeRegistry, FederationManager, TrustHandshake, SyncProtocol
from kcn_v6.model_interoperability import ModelAdapter, LLMGateway, EmbeddingBridge, InferenceRouter
from kcn_v6.universal_agent_identity import AgentIdentity, CapabilityCertificate, ReputationHistory, PermissionScope
from kcn_v6.benchmark_exchange import BenchmarkRegistry, EvaluationExchange, ScoringEngine, LeaderboardManager
from kcn_v6.research_network import ExperimentRegistry, PaperTracker, DiscoveryExchange, CollaborationEngine

__all__ = [
    "IntelligenceMessage", "AgentCommunication", "CapabilityProtocol", "ContextExchange",
    "NodeRegistry", "FederationManager", "TrustHandshake", "SyncProtocol",
    "ModelAdapter", "LLMGateway", "EmbeddingBridge", "InferenceRouter",
    "AgentIdentity", "CapabilityCertificate", "ReputationHistory", "PermissionScope",
    "BenchmarkRegistry", "EvaluationExchange", "ScoringEngine", "LeaderboardManager",
    "ExperimentRegistry", "PaperTracker", "DiscoveryExchange", "CollaborationEngine"
]

"""
KCN v4 Knowledge Network Subpackage.
Provenance chains, global graph querying, asynchronous replication, and evidence consensus voting.
"""

from kcn_v4.knowledge_network.provenance_chain import ProvenanceChain
from kcn_v4.knowledge_network.global_graph import GlobalKnowledgeGraph
from kcn_v4.knowledge_network.knowledge_replication import KnowledgeReplicationEngine
from kcn_v4.knowledge_network.evidence_consensus import EvidenceConsensusVoter

__all__ = [
    "ProvenanceChain",
    "GlobalKnowledgeGraph",
    "KnowledgeReplicationEngine",
    "EvidenceConsensusVoter",
]

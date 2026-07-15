"""
KCN v4 Research Network Subpackage.
Global experiment exchange, breakthrough discovery registry, cross-institutional collaboration, and publication citation tracking.
"""

from kcn_v4.research_network.experiment_exchange import ResearchExchange
from kcn_v4.research_network.discovery_registry import DiscoveryRegistry
from kcn_v4.research_network.collaboration_engine import ResearchCollaborationEngine
from kcn_v4.research_network.publication_tracker import PublicationTracker

__all__ = [
    "ResearchExchange",
    "DiscoveryRegistry",
    "ResearchCollaborationEngine",
    "PublicationTracker",
]

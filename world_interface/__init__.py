"""
Phase 121 - Real-Time World Interface Package.
The sensory organs ingesting live data, API connectors, document parsing, reality feeds, and freshness sync.
"""

from world_interface.data_ingestion import RealTimeDataIngestion
from world_interface.reality_sync import RealitySyncEngine

__all__ = ["RealTimeDataIngestion", "RealitySyncEngine"]

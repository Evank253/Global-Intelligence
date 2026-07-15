"""
Phase 18 - Production Data Fabric & Knowledge Infrastructure Package.
Subpackages: ingestion_engine, validation_layer, knowledge_storage, retrieval_engine, governance.
"""

from data_fabric.ingestion_engine.document_ingestion import DocumentIngestionPipeline
from data_fabric.validation_layer.provenance_tracker import ProvenanceTracker
from data_fabric.validation_layer.quality_scoring import DataQualityScorer
from data_fabric.knowledge_storage.graph_database import GraphDatabaseAdapter
from data_fabric.knowledge_storage.vector_memory import VectorMemoryAdapter
from data_fabric.knowledge_storage.archival_vault import PersistentArchivalVault
from data_fabric.retrieval_engine.hybrid_search import HybridSearchEngine
from data_fabric.governance.access_control import DataAccessControl

__all__ = [
    "DocumentIngestionPipeline",
    "ProvenanceTracker",
    "DataQualityScorer",
    "GraphDatabaseAdapter",
    "VectorMemoryAdapter",
    "PersistentArchivalVault",
    "HybridSearchEngine",
    "DataAccessControl",
]

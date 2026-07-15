"""
Data Fabric - Knowledge Storage Subpackage.
Graph database abstraction, vector embeddings store, relational ledger, and persistent archival vault.
"""

from data_fabric.knowledge_storage.graph_database import GraphDatabaseAdapter
from data_fabric.knowledge_storage.vector_memory import VectorMemoryAdapter
from data_fabric.knowledge_storage.relational_storage import RelationalStorageAdapter
from data_fabric.knowledge_storage.archival_vault import PersistentArchivalVault

__all__ = [
    "GraphDatabaseAdapter",
    "VectorMemoryAdapter",
    "RelationalStorageAdapter",
    "PersistentArchivalVault",
]

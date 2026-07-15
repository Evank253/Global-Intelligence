"""
Knowledge Repository - Unified interface fusing Relational and Vector Memory.
"""

from typing import Dict, Any, List
from memory.database.postgres_adapter import PostgresMemory
from memory.database.vector_store import VectorMemory


class KnowledgeRepository:
    def __init__(self):
        self.postgres = PostgresMemory()
        self.vector_mem = VectorMemory()

    def store_fact_with_embedding(self, table: str, text: str, embedding: List[float]) -> str:
        vec_id = self.vector_mem.insert(text, embedding)
        self.postgres.save_record(table, {"vec_id": vec_id, "text": text})
        return vec_id

"""
Vector Memory - In-Memory and Embedded Vector Similarity Index.
"""

import uuid
from typing import Dict, Any, List


class VectorMemory:
    def __init__(self):
        self.index: Dict[str, Dict[str, Any]] = {}

    def insert(self, text: str, embedding: List[float]) -> str:
        item_id = str(uuid.uuid4())
        self.index[item_id] = {
            "text": text,
            "embedding": embedding,
        }
        return item_id

    def search(self, vector: List[float]) -> List[Dict[str, Any]]:
        return list(self.index.values())

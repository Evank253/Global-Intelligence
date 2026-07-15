"""
KCN v6 Model Interoperability - Embedding Bridge
"""

from typing import List


class EmbeddingBridge:
    def align_embeddings(self, source_vector: List[float], source_dim: int, target_dim: int) -> List[float]:
        if source_dim == target_dim:
            return source_vector
        return (source_vector * (target_dim // source_dim + 1))[:target_dim]

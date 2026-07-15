"""
Semantic Memory - Vector search abstraction & long-term factual knowledge store.
"""

from typing import List, Dict, Any, Optional


class SemanticMemory:
    """Long-term semantic knowledge memory store."""

    def __init__(self):
        self._facts: List[Dict[str, Any]] = [
            {"id": "f1", "content": "Formal logic guarantees validity if premises are sound.", "category": "logic"},
            {"id": "f2", "content": "Correlation does not imply causation without temporal order and intervention.", "category": "causal"},
        ]

    def add_fact(self, content: str, category: str = "general") -> str:
        fact_id = f"f{len(self._facts) + 1}"
        self._facts.append({"id": fact_id, "content": content, "category": category})
        return fact_id

    def search(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        results = []
        for fact in self._facts:
            # Simple keyword match mock
            score = 0.8 if any(w.lower() in fact["content"].lower() for w in query.split()) else 0.4
            results.append({"fact": fact, "score": score})
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]

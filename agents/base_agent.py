"""
KCN Intelligence OS - Base Agent Interface
Abstract Base Class defining standard interface, metadata, scoring, and lifecycle hooks for all intelligence agents.
"""

from abc import ABC, abstractmethod
import time
from typing import Dict, Any, List, Optional


class BaseAgent(ABC):
    """Abstract Base Class for all specialized system agents."""

    def __init__(self, name: str, role: str, category: str = "general"):
        self.name = name
        self.role = role
        self.category = category
        self.performance: List[Dict[str, Any]] = []
        self.capabilities: List[str] = []
        self.created_at: float = time.time()

    @abstractmethod
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process input data and produce agent output."""
        pass

    def score(self, result: Dict[str, Any]) -> None:
        """Record a performance evaluation result."""
        result["timestamp"] = time.time()
        self.performance.append(result)

    def get_average_score(self) -> float:
        """Calculate average score across recorded performances."""
        if not self.performance:
            return 0.0
        scores = [p.get("score", 0.0) for p in self.performance if "score" in p]
        return sum(scores) / len(scores) if scores else 0.0

    def to_dict(self) -> Dict[str, Any]:
        """Export agent status and metadata."""
        return {
            "name": self.name,
            "role": self.role,
            "category": self.category,
            "capabilities": self.capabilities,
            "total_runs": len(self.performance),
            "average_score": self.get_average_score(),
        }

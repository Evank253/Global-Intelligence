"""
KCN Intelligence OS - Question Decomposer
Decomposes high-level prompts into actionable atomic sub-questions.
"""

from typing import List, Dict, Any


class QuestionDecomposer:
    """Decomposes a user query into ordered atomic sub-questions."""

    def decompose(self, query: str) -> List[Dict[str, Any]]:
        """Decomposes query into atomic questions with dependency tags."""
        sub_questions = [
            {
                "id": 1,
                "question": f"Core definitions and direct scope of: '{query}'",
                "type": "definitional",
                "depends_on": [],
            },
            {
                "id": 2,
                "question": f"Underlying causal mechanisms involved in: '{query}'",
                "type": "causal",
                "depends_on": [1],
            },
            {
                "id": 3,
                "question": f"Systemic trade-offs, risks, and failure modes regarding: '{query}'",
                "type": "risk_analysis",
                "depends_on": [1, 2],
            },
            {
                "id": 4,
                "question": f"Optimal decision synthesis and action recommendations for: '{query}'",
                "type": "synthesis",
                "depends_on": [2, 3],
            },
        ]
        return sub_questions

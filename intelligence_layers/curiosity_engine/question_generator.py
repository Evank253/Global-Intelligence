"""
Question Generator - Formulates focused clarifying questions for information retrieval.
"""

from typing import List, Dict, Any


class QuestionGenerator:
    """Generates probing research questions to resolve identified gaps."""

    def generate_questions_for_gaps(self, gaps: List[Dict[str, Any]]) -> List[str]:
        questions = []
        for gap in gaps:
            questions.append(f"What specific facts or data exist for branch '{gap.get('missing_branch')}'?")
        return questions

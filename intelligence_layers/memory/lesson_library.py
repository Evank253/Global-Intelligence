"""
Lesson Library - Distilled generalizations and heuristics extracted from past experiences.
"""

from typing import List, Dict, Any


class LessonLibrary:
    """Library of generalized principles derived from past system runs."""

    def __init__(self):
        self.lessons = [
            "Always verify premise independence before applying joint probabilities.",
            "In high-uncertainty domains, prioritize falsifiable hypotheses over speculative generative models.",
        ]

    def add_lesson(self, lesson: str) -> None:
        if lesson not in self.lessons:
            self.lessons.append(lesson)

    def get_lessons(self) -> List[str]:
        return self.lessons

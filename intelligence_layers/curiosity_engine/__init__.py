"""
Curiosity Engine subpackage initialization.
"""
from intelligence_layers.curiosity_engine.gap_detector import GapDetector
from intelligence_layers.curiosity_engine.question_generator import QuestionGenerator
from intelligence_layers.curiosity_engine.research_planner import ResearchPlanner

__all__ = ["GapDetector", "QuestionGenerator", "ResearchPlanner"]

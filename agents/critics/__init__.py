"""
Critics subpackage initialization.
"""
from agents.critics.skeptic_agent import SkepticAgent
from agents.critics.bias_detector import BiasDetector
from agents.critics.adversary_agent import AdversaryAgent

__all__ = ["SkepticAgent", "BiasDetector", "AdversaryAgent"]

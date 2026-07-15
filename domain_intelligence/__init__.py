"""
v0.6 Universal Domain Expert Swarm Subpackage.
Contains specialized expert agents across Mathematics, Physics, Medicine, Biology, Law, Engineering, Finance, Writing, Design, Astronomy, Geography, and Philosophy.
"""

from domain_intelligence.math_expert import MathExpertAgent
from domain_intelligence.physics_expert import PhysicsExpertAgent
from domain_intelligence.medicine_expert import MedicineExpertAgent
from domain_intelligence.biology_expert import BiologyExpertAgent
from domain_intelligence.law_expert import LawExpertAgent
from domain_intelligence.engineering_expert import EngineeringExpertAgent
from domain_intelligence.finance_expert import FinanceExpertAgent
from domain_intelligence.writing_expert import WritingExpertAgent
from domain_intelligence.design_expert import DesignExpertAgent
from domain_intelligence.astronomy_expert import AstronomyExpertAgent
from domain_intelligence.geography_expert import GeographyExpertAgent
from domain_intelligence.philosophy_expert import PhilosophyExpertAgent

__all__ = [
    "MathExpertAgent",
    "PhysicsExpertAgent",
    "MedicineExpertAgent",
    "BiologyExpertAgent",
    "LawExpertAgent",
    "EngineeringExpertAgent",
    "FinanceExpertAgent",
    "WritingExpertAgent",
    "DesignExpertAgent",
    "AstronomyExpertAgent",
    "GeographyExpertAgent",
    "PhilosophyExpertAgent",
]

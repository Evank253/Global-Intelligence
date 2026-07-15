"""
KCN v8 - Sim-to-Real Validation Subpackage
Simulation-to-reality gap analysis, domain randomization, physical bench testing, and reality verification.
"""

from kcn_v8.sim2real_validation.gap_analyzer import GapAnalyzer
from kcn_v8.sim2real_validation.domain_randomization import DomainRandomization
from kcn_v8.sim2real_validation.real_world_bench import RealWorldBench
from kcn_v8.sim2real_validation.reality_verifier import RealityVerifier

__all__ = ["GapAnalyzer", "DomainRandomization", "RealWorldBench", "RealityVerifier"]

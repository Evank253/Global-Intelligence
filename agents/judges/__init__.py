"""
Judges subpackage initialization.
"""
from agents.judges.truth_judge import TruthJudge
from agents.judges.evidence_judge import EvidenceJudge
from agents.judges.logic_judge import LogicJudge
from agents.judges.safety_judge import SafetyJudge
from agents.judges.reality_judge import RealityJudge
from agents.judges.judge_council import JudgeCouncil

__all__ = [
    "TruthJudge",
    "EvidenceJudge",
    "LogicJudge",
    "SafetyJudge",
    "RealityJudge",
    "JudgeCouncil",
]

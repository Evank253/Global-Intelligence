"""
KCN Intelligence OS - Judge Council
Aggregates evaluations across all specialized judges to score and rank candidates.
"""

from typing import List, Dict, Any
from agents.base_agent import BaseAgent
from agents.judges.truth_judge import TruthJudge
from agents.judges.evidence_judge import EvidenceJudge
from agents.judges.logic_judge import LogicJudge
from agents.judges.safety_judge import SafetyJudge
from agents.judges.reality_judge import RealityJudge


class JudgeCouncil(BaseAgent):
    """Council coordinating individual judge evaluations and computing overall candidate rankings."""

    def __init__(self, name: str = "JudgeCouncil", role: str = "Multi-Judge Decision Council"):
        super().__init__(name=name, role=role, category="judge")
        self.truth_judge = TruthJudge()
        self.evidence_judge = EvidenceJudge()
        self.logic_judge = LogicJudge()
        self.safety_judge = SafetyJudge()
        self.reality_judge = RealityJudge()

    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        answers = input_data.get("answers", [])
        judged_answers = self.evaluate(answers)
        return {
            "council": self.name,
            "evaluated_count": len(judged_answers),
            "ranked_answers": judged_answers,
        }

    def evaluate(self, answers: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Evaluates and ranks candidate answers using judge scores."""
        for answer in answers:
            # Execute individual judges
            t_res = self.truth_judge.process(answer)
            e_res = self.evidence_judge.process(answer)
            l_res = self.logic_judge.process(answer)
            s_res = self.safety_judge.process(answer)
            r_res = self.reality_judge.process(answer)

            raw_scores = answer.get("score", {})
            evidence_score = raw_scores.get("evidence", e_res["score"])
            logic_score = raw_scores.get("logic", l_res["score"])
            impact_score = raw_scores.get("impact", r_res["score"])
            safety_score = raw_scores.get("safety", s_res["score"])

            # Compute composite final score
            answer["judge_breakdown"] = {
                "truth": t_res["score"],
                "evidence": evidence_score,
                "logic": logic_score,
                "safety": safety_score,
                "reality": impact_score,
            }

            answer["final_score"] = round(
                (evidence_score * 0.25)
                + (logic_score * 0.25)
                + (impact_score * 0.25)
                + (safety_score * 0.25),
                3,
            )

        return sorted(
            answers,
            key=lambda x: x.get("final_score", 0),
            reverse=True,
        )

"""
Unit and integration tests for Reasoning Engines and Swarm Agents.
"""

import pytest
from core.kernel import Kernel
from core.orchestrator import Orchestrator
from reasoning_engine.tree_engine import ReasoningTree
from reasoning_engine.question_decomposer import QuestionDecomposer
from reasoning_engine.hypothesis_engine import HypothesisEngine
from reasoning_engine.elimination_engine import EliminationEngine
from reasoning_engine.debate_engine import DebateEngine
from agents.reasoning.logic_agent import LogicAgent
from agents.judges.judge_council import JudgeCouncil


def test_tree_engine_construction():
    tree_engine = ReasoningTree()
    tree = tree_engine.build("How to optimize system performance?")
    assert tree["question"] == "How to optimize system performance?"
    assert "what" in tree["branches"]
    assert len(tree["branches"]) == 9


def test_question_decomposition():
    decomposer = QuestionDecomposer()
    sub_qs = decomposer.decompose("What are the risks of AI scaling?")
    assert len(sub_qs) == 4
    assert sub_qs[0]["type"] == "definitional"


def test_hypothesis_generation_and_elimination():
    hyp_engine = HypothesisEngine()
    elim_engine = EliminationEngine()

    hypotheses = hyp_engine.generate(["what", "why", "risks"])
    assert len(hypotheses) == 3

    eliminated, retained = elim_engine.evaluate_and_eliminate(hypotheses)
    assert len(retained) + len(eliminated) == 3


def test_debate_engine_and_judge_council():
    debate_engine = DebateEngine()
    council = JudgeCouncil()

    candidates = [
        {"confidence": 0.8, "hypothesis": "Candidate A"},
        {"confidence": 0.6, "hypothesis": "Candidate B"},
    ]

    debate_results = debate_engine.debate(candidates)
    assert len(debate_results) == 2

    ranked = council.evaluate(debate_results)
    assert ranked[0]["final_score"] >= ranked[1]["final_score"]


def test_end_to_end_orchestrator_flow():
    kernel = Kernel()
    kernel.registry.register(LogicAgent(), category="reasoning")
    kernel.registry.register(JudgeCouncil(), category="judge")

    orchestrator = Orchestrator(kernel)
    result = orchestrator.process_query("What is the impact of quantum computing on cryptography?")

    assert result["status"] == "SUCCESS"
    assert "session_id" in result
    assert "top_candidate" in result
    assert "confidence_report" in result

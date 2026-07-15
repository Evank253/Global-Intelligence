"""
KCN Intelligence OS - v5, v6, v7 Apex Subsystems Test Suite
Tests Autonomous Governance (v5), Interoperability Layer (v6), and Autonomous Scientific Discovery Engine (v7).
"""

import pytest

from kcn_v5 import PolicyEngine, TrustScoreEngine, ImprovementValidator, EvidenceGraph, ScenarioEngine, GlobalHealth
from kcn_v6 import IntelligenceMessage, NodeRegistry, AgentIdentity, LLMGateway, BenchmarkRegistry, ExperimentRegistry
from kcn_v7 import (
    HypothesisEngine, ResearchQuestionEngine, NoveltyDetector, IdeaRanker,
    ExperimentDesigner, SimulationRunner, ParameterOptimizer, ResultAnalyzer,
    LiteratureMapper, EvidenceEvaluator, ContradictionDetector, TheoryComparator,
    ResearchRegistry, DatasetTracker, SeedManager, ReplicationEngine,
    ResearchPaperBuilder, CitationManager, PeerReviewAgent, ResearchArchive,
    EthicsReview, SafetyConstraints, ApprovalGate, DiscoveryAudit
)


def test_v5_autonomous_governance_and_trust():
    policy = PolicyEngine()
    policy.add_rule("Zero Black Box Rule", "black_box_risk_score == 0.00")
    eval_res = policy.evaluate("execute_query")
    assert eval_res["approved"] is True

    trust = TrustScoreEngine()
    trust_res = trust.calculate("Node_01")
    assert trust_res["trust_score"] == 1.0

    validator = ImprovementValidator()
    val_res = validator.compare(0.85, 0.92)
    assert val_res["accepted"] is True

    evidence = EvidenceGraph()
    ev = evidence.add_evidence("Cellular feedback stabilizes power grids", "bio_physics_swarm")
    assert ev["claim"] == "Cellular feedback stabilizes power grids"

    scenario = ScenarioEngine()
    sim = scenario.simulate("Grid Surge Test")
    assert "best_case" in sim["outcomes"]

    health = GlobalHealth.status()
    assert health["nodes"] == "operational"


def test_v6_universal_interoperability_layer():
    msg = IntelligenceMessage(sender="Agent_Alpha", receiver="Agent_Beta", objective="Sync state", payload={"key": "val"})
    serialized = msg.serialize()
    assert serialized["sender"] == "Agent_Alpha"
    assert serialized["id"] is not None

    registry = NodeRegistry()
    registry.register("node_100", ["math", "physics"])
    discovered = registry.discover("math")
    assert "node_100" in discovered

    identity = AgentIdentity()
    agent_id = identity.create("Logic_Agent", ["deduction"])
    assert "fingerprint" in agent_id

    gateway = LLMGateway()
    gateway.register_model("KCN", "v6_model")
    routed = gateway.route("Task 1")
    assert routed["selected_model"]["model"] == "v6_model"

    bench = BenchmarkRegistry()
    bench.publish({"name": "ECE Calibration Test", "bound": 0.035})
    assert len(bench.list_all()) == 1

    exp = ExperimentRegistry()
    res = exp.submit("Decoherence Suppression", {"fidelity": 0.999})
    assert res is True


def test_v7_autonomous_scientific_discovery_engine():
    # 1. Discovery Engine
    hyp_engine = HypothesisEngine()
    hyp = hyp_engine.create("Cellular frequency dampening in heart tissue", "Transferable to high-voltage microgrid controllers")
    assert hyp["status"] == "unverified"
    assert len(hyp_engine.list()) == 1

    rq_engine = ResearchQuestionEngine()
    questions = rq_engine.formulate_questions("high voltage surge dampening")
    assert len(questions) > 0

    # 2. Experiment Engine
    designer = ExperimentDesigner()
    exp_spec = designer.design(hyp, variables=["voltage_freq", "dampening_coef"], controls=["baseline_grid"])
    assert exp_spec["method"] == "controlled simulation"

    runner = SimulationRunner()
    sim_out = runner.run(exp_spec, iterations=10)
    assert sim_out["iterations"] == 10
    assert len(sim_out["results"]) == 10

    analyzer = ResultAnalyzer()
    analysis = analyzer.analyze_simulation(sim_out)
    assert analysis["p_value"] < 0.05

    # 3. Scientific Reasoning & Evidence Evaluator
    evaluator = EvidenceEvaluator()
    ev_score = evaluator.score([{"quality": 0.95}, {"quality": 0.98}])
    assert ev_score["evidence_score"] > 0.90

    # 4. Reproducibility Layer
    research_reg = ResearchRegistry()
    research_reg.register("Bio-Grid Experiment", sim_out, seed=42)
    assert len(research_reg.records) == 1
    assert research_reg.records[0]["seed"] == 42

    seed_mgr = SeedManager()
    seed_info = seed_mgr.set_global_seed(42)
    assert seed_info["deterministic_reproducibility"] is True

    # 5. Publication Pipeline
    paper_builder = ResearchPaperBuilder()
    draft = paper_builder.generate(
        title="Bio-Inspired Microgrid Cascade Mitigation",
        abstract="Negative feedback dampening suppresses peak load oscillations.",
        findings=analysis
    )
    assert draft["status"] == "draft"

    peer_agent = PeerReviewAgent()
    review = peer_agent.review_paper(draft)
    assert review["decision"] == "ACCEPT_WITH_EXCELLENCE"

    # 6. Scientific Governance Gate
    gate = ApprovalGate()
    approval = gate.review(draft)
    assert approval["approval_required"] is True
    assert approval["state"] == "awaiting_review"

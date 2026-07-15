"""
Unit and integration test suite for KCN v4 Global Intelligence Network Layer.
Tests Federated Intelligence Nodes, Provenance Chain, Agent Reputation & Economy, Compute Fabric, Research Network, and Global Mission Control.
"""

import pytest
from kcn_v4.federated_intelligence.node_registry import IntelligenceNodeRegistry
from kcn_v4.federated_intelligence.intelligence_sync import IntelligenceSyncEngine
from kcn_v4.federated_intelligence.trust_handshake import TrustHandshakeProtocol
from kcn_v4.federated_intelligence.distributed_reasoning import DistributedReasoningEngine

from kcn_v4.knowledge_network.provenance_chain import ProvenanceChain
from kcn_v4.knowledge_network.global_graph import GlobalKnowledgeGraph
from kcn_v4.knowledge_network.evidence_consensus import EvidenceConsensusVoter

from kcn_v4.agent_economy.reputation_engine import AgentReputation
from kcn_v4.agent_economy.agent_market import AgentMarketplace
from kcn_v4.agent_economy.contribution_rewards import ContributionRewardAllocator

from kcn_v4.compute_fabric.workload_orchestrator import ComputeOrchestrator
from kcn_v4.compute_fabric.gpu_scheduler import GPUScheduler

from kcn_v4.research_network.experiment_exchange import ResearchExchange
from kcn_v4.research_network.discovery_registry import DiscoveryRegistry

from kcn_v4.global_operations.mission_control import MissionControl
from kcn_v4.global_operations.impact_measurement import ImpactMeasurement


def test_v4_federated_intelligence():
    nodes = IntelligenceNodeRegistry()
    sync = IntelligenceSyncEngine()
    handshake = TrustHandshakeProtocol()
    dist = DistributedReasoningEngine()

    node_id = nodes.register_node("ResearchLab_Alpha", ["formal_logic", "quantum_sim"])
    assert len(nodes.list_nodes()) == 1

    s_res = sync.sync_nodes(node_id, "Node_Beta")
    assert s_res["sync_status"] == "SYNCHRONIZED_ACTIVE"

    h_res = handshake.verify_handshake(node_id, "sig_trust_101")
    assert h_res["handshake"] == "ESTABLISHED"

    d_res = dist.dispatch_federated_query("Quantum Energy Optimization", [node_id, "Node_Beta"])
    assert d_res["nodes_queried"] == 2


def test_v4_knowledge_network_and_provenance():
    prov = ProvenanceChain()
    graph = GlobalKnowledgeGraph()
    voter = EvidenceConsensusVoter()

    rec = prov.create_record("Verified quantum grid state")
    assert rec["verified"] is True

    g_res = graph.query_global_network_graph("Grid Isomorphism")
    assert g_res["graph_health"] == "GLOBALLY_SYNCHRONIZED"

    votes = [{"node": "n1", "vote": True}, {"node": "n2", "vote": True}, {"node": "n3", "vote": False}]
    c_res = voter.evaluate_multi_node_consensus(votes)
    assert c_res["consensus_status"] == "GLOBAL_CONSENSUS_ACHIEVED"


def test_v4_agent_economy():
    rep = AgentReputation()
    market = AgentMarketplace()
    rewards = ContributionRewardAllocator()

    score = rep.update("CausalAgent_Alpha", True)
    assert score == 101

    score_fail = rep.update("CausalAgent_Alpha", False)
    assert score_fail == 96

    listing = market.list_capability("LogicAgent_Beta", "Modal Logic Verification", 10)
    assert listing["cost"] == 10

    reward = rewards.allocate_token_reward("ResearchNode_01", 0.95)
    assert reward["tokens_rewarded"] == 95.0


def test_v4_compute_fabric_and_research():
    compute = ComputeOrchestrator()
    gpu = GPUScheduler()
    research = ResearchExchange()
    discovery = DiscoveryRegistry()

    alloc = compute.allocate("Quantum_Simulation_Job_101")
    assert alloc["status"] == "running"

    gpu_res = gpu.schedule_gpu_cluster(64.0)
    assert gpu_res["allocated_gpus"] == 8

    exp = research.submit({"id": "exp_01", "title": "Microgrid Islanding Test"})
    assert exp["submitted"] is True

    disc = discovery.register_breakthrough("Zero-Lag Microgrid Islanding", "Energy", ["Paper 1"])
    assert disc["verified"] is True


def test_v4_global_operations():
    control = MissionControl()
    impact = ImpactMeasurement()

    m_res = control.execute("Global Decarbonization Initiative")
    assert m_res["status"] == "coordinated"
    assert len(m_res["systems"]) == 4

    imp_res = impact.measure_civilization_impact("Deploying biomimetic islanding microgrids")
    assert imp_res["impact_rating"] == "STRONGLY_BENEFICIAL"

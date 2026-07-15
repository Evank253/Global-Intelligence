"""
KCN Intelligence OS v4 - Main Entrypoint & System Demonstration
Boots Kernel, executes Master Domain Orchestration, Federated Node Sync, Agent Economy Reputation, Compute Scheduling, and Mission Control.
"""

import sys
import logging
import json
import time

from core.kernel import Kernel
from core.orchestrator import Orchestrator
from agents.reasoning.logic_agent import LogicAgent
from agents.reasoning.causal_agent import CausalAgent
from agents.reasoning.systems_agent import SystemsAgent
from agents.reasoning.hypothesis_agent import HypothesisAgent
from agents.teachers.knowledge_teacher import KnowledgeTeacher
from agents.teachers.reasoning_teacher import ReasoningTeacher
from agents.teachers.safety_teacher import SafetyTeacher
from agents.teachers.ethics_teacher import EthicsTeacher
from agents.judges.judge_council import JudgeCouncil
from agents.critics.skeptic_agent import SkepticAgent
from agents.critics.bias_detector import BiasDetector

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)

logger = logging.getLogger("KCN.Main")


def main():
    print("=" * 80)
    print("      KCN INTELLIGENCE OS v4 - GLOBAL INTELLIGENCE NETWORK PLATFORM")
    print("=" * 80)

    # 1. Boot System Kernel
    logger.info("Booting KCN Kernel...")
    kernel = Kernel()

    # 2. Register Swarm Agents
    logger.info("Registering Swarm Agents...")
    kernel.registry.register(LogicAgent(), category="reasoning")
    kernel.registry.register(CausalAgent(), category="reasoning")
    kernel.registry.register(SystemsAgent(), category="reasoning")
    kernel.registry.register(HypothesisAgent(), category="reasoning")
    kernel.registry.register(KnowledgeTeacher(), category="teacher")
    kernel.registry.register(ReasoningTeacher(), category="teacher")
    kernel.registry.register(SafetyTeacher(), category="teacher")
    kernel.registry.register(EthicsTeacher(), category="teacher")
    kernel.registry.register(JudgeCouncil(), category="judge")
    kernel.registry.register(SkepticAgent(), category="critic")
    kernel.registry.register(BiasDetector(), category="critic")

    status = kernel.get_system_status()
    print(f"\n[System Diagnostic] Status: {status['status']} | Active Agents: {status['registered_agents']} | Target Milestone: v4 Network")

    # 3. Instantiate Pipeline Orchestrator
    orchestrator = Orchestrator(kernel)

    # 4. Process Demonstration Query
    sample_query = "How can we transfer cellular immunology resilience principles to stabilize power microgrid cascades against extreme weather events?"
    print("\n" + "-" * 80)
    print(f"EXECUTING QUERY UNDER KCN v4 DISTRIBUTED NETWORK DIRECTIVES: '{sample_query}'")
    print("-" * 80)

    start_time = time.time()
    result = orchestrator.process_query(sample_query, context={"api_key": "key_enterprise_alpha"})
    elapsed = time.time() - start_time

    print(f"\n[Execution Summary] Status: {result['status']} | Milestone: {result['phase_milestone']} | Time: {elapsed:.3f}s")

    print("\n1. KCN v4 Global Network Operations:")
    v4 = result.get("kcn_v4_network", {})
    print(f"   - Mission Control Status: {v4.get('mission_control')}")
    print(f"   - Provenance Chain Hash: {v4.get('provenance_chain_hash')}")
    print(f"   - Assigned Compute Node: {v4.get('compute_assigned')}")

    print("\n2. Phase 19 Agent Runtime Controlled Execution:")
    runtime = result.get("agent_runtime", {})
    print(f"   - Process State: {runtime.get('process_state')}")
    print(f"   - Scheduled Task ID: {runtime.get('scheduled_task_id')}")

    print("\n3. Phase 18 Production Data Fabric:")
    df = result.get("data_fabric", {})
    print(f"   - Quality Score: {df.get('quality_score')}")
    print(f"   - Provenance Signature: {df.get('provenance_signature')}")

    print("\n4. Phase 150 Master Decision Fusion Verdict:")
    master = result.get("master_verdict", {})
    print(f"   - Consensus Verdict: {master.get('consensus_verdict')}")
    print(f"   - Aggregate Evidence Strength: {master.get('aggregate_evidence_strength')}")

    print("\n" + "=" * 80)
    print("      KCN v4 NETWORK ACTIVE. REST API available via 'python api/server.py'")
    print("=" * 80)


if __name__ == "__main__":
    main()

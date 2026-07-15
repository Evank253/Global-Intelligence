"""
Unit and integration tests for Phases 94-100: KCN Unified Organism Architecture.
Tests DNA, Heart, Brain, Kronos Arms, Reality Legs, Nervous System, and KCN-AKIIS Immune System.
"""

import pytest
from core.kernel import Kernel
from core.orchestrator import Orchestrator
from dna_engine.genome import DNAEngine
from nervous_system.organism_bus import OrganismNervousSystem
from kcn_akiis.teacher_student import TeacherStudentSystem
from kcn_akiis.benchmark_engine import BenchmarkEngine
from kcn_akiis.performance_report import PerformanceReportGenerator
from kronos_builder.software_architect import SoftwareArchitectAgent
from kronos_builder.coder_agents import CoderAgentsSuite
from kronos_builder.code_redteam import CodeRedTeam
from kronos_builder.software_benchmark_lab import SoftwareBenchmarkLab
from reality_operations.deployment_systems import DeploymentSystems
from reality_operations.outcome_tracker import OutcomeTracker
from organism_core.unified_organism import UnifiedOrganismCore


def test_dna_engine():
    dna = DNAEngine()
    genome = dna.inspect_genome()
    assert genome["genome_version"] == "1.100.0-UNIFIED-ORGANISM"
    assert "BRAIN" in genome["organs_registered"]
    assert "ARMS" in genome["organs_registered"]


def test_nervous_system():
    nervous = OrganismNervousSystem()
    signal = nervous.transmit_signal("BRAIN", "ARMS", "BUILD_APP", {"app_id": "app_01"})
    assert signal["source"] == "BRAIN"
    assert signal["target"] == "ARMS"
    assert nervous.get_nervous_health()["total_signals_propagated"] == 1


def test_kcn_akiis_immune_system():
    teacher_student = TeacherStudentSystem()
    bench = BenchmarkEngine()
    reporter = PerformanceReportGenerator()

    ts_eval = teacher_student.evaluate_knowledge_transfer("StudentAgent_A", "Causal Reasoning", pre_score=0.60, post_score=0.92)
    assert ts_eval["knowledge_transfer_percentage"] == "92.0%"
    assert ts_eval["mastery_status"] == "MASTERED"

    sweep = bench.run_global_benchmark_sweep()
    assert sweep["composite_immune_score"] > 0.85

    card = reporter.generate_report("v1.100.0", sweep["metrics"], ts_eval)
    assert card["overall_trajectory"]["intelligence_score"] == 0.935


def test_kronos_vibe_coder_arms():
    architect = SoftwareArchitectAgent()
    coders = CoderAgentsSuite()
    red_team = CodeRedTeam()
    lab = SoftwareBenchmarkLab()

    arch = architect.design_system_architecture("Microgrid Energy API")
    assert arch["technical_debt_score"] == 0.05

    code = coders.synthesize_application_code(arch)
    assert len(code["modules_generated"]) == 5

    redteam = red_team.attack_codebase(code["synthesized_code_sample"])
    assert redteam["vulnerabilities_found"] == 0

    bench = lab.benchmark_software_system(code)
    assert bench["benchmark_passed"] is True


def test_reality_operations_legs():
    deployer = DeploymentSystems()
    tracker = OutcomeTracker()

    dep = deployer.deploy_to_staging({"code": "sample"})
    assert dep["deployment_status"] == "ONLINE_HEALTHY"

    outcome = tracker.record_and_compare(predicted_impact=0.90, observed_impact=0.92)
    assert outcome["real_world_accuracy_score"] == 0.98


def test_unified_organism_full_closed_loop():
    kernel = Kernel()
    orchestrator = Orchestrator(kernel)
    organism = UnifiedOrganismCore(orchestrator_ref=orchestrator)

    cycle_result = organism.execute_organism_cycle("Build a resilient edge microgrid controller application")

    assert cycle_result["organism_status"] == "CLOSED_LOOP_SUCCESS"
    assert cycle_result["arms_kronos_builder"]["security_clearance"] == "PASSED_HIGH_RESILIENT"
    assert cycle_result["immune_kcn_akiis"]["composite_immune_score"] > 0.80
    assert cycle_result["legs_reality_operations"]["deployment_status"] == "ONLINE_HEALTHY"
    assert cycle_result["nervous_system_telemetry"]["total_signals_propagated"] == 4

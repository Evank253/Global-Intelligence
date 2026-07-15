"""
Unit tests for KCN Intelligence OS v2 Orchestrator and API Command Center.
"""

import pytest
from core.kcn_orchestrator import KCNOrchestrator
from core.organism_kernel import OrganismKernel
from core.executive_cortex import ExecutiveCortexController
from core.dna_engine import DNAEvolutionEngine


def test_v2_kcn_orchestrator_health_and_execute():
    orchestrator = KCNOrchestrator()
    health = orchestrator.health()

    assert health["system"] == "KCN Intelligence OS v2"
    assert health["status"] == "HEALTHY"
    assert health["components"]["core"] == "online"

    execution = orchestrator.execute("Analyze global infrastructure optimization")
    assert execution["status"] == "completed"
    assert len(execution["pipeline"]) == 7
    assert execution["trust_score"] == 0.985


def test_v2_core_subsystems():
    kernel = OrganismKernel()
    cortex = ExecutiveCortexController()
    dna = DNAEvolutionEngine()

    diag = kernel.get_kernel_diagnostics()
    assert diag["kernel_version"] == "v2.0.0-HARDENED"

    route = cortex.route_and_allocate("Optimize city power network")
    assert "science" in route["allocated_domains"]

    genome = dna.inspect_genome()
    assert genome["integrity_status"] == "PERFECT_GENOME_MATCH"

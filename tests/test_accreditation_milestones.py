"""
Unit and integration test verifying the 12 Major Milestones and Research Package completeness.
"""

import os
import pytest
from core.kernel import Kernel
from core.orchestrator import Orchestrator


def test_research_package_documentation_exists():
    research_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "research")
    required_files = [
        "architecture_paper.md",
        "benchmark_methodology.md",
        "safety_framework.md",
        "limitations.md",
        "reproducibility_guide.md",
        "datasets.md",
    ]

    for fname in required_files:
        path = os.path.join(research_dir, fname)
        assert os.path.exists(path), f"Missing research package document: {fname}"
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            assert len(content) > 100, f"Research document {fname} is empty or insufficient."


def test_12_milestone_subsystem_readiness():
    kernel = Kernel()
    orchestrator = Orchestrator(kernel)

    # Verify key milestone engines are instantiated
    assert orchestrator.cortex is not None, "Milestone 1 Core Kernel & Cortex"
    assert orchestrator.validation_harness is not None, "Milestone 2 KCN-AKIIS Immune & Reality Validation"
    assert orchestrator.engineering_lab is not None, "Milestone 3 Kronos Engineering Arms"
    assert orchestrator.vault is not None, "Milestone 4 Knowledge Preservation Vault"
    assert orchestrator.theory_engine is not None, "Milestone 5 Research & Theory Engine"
    assert orchestrator.reputation_engine is not None, "Milestone 6 Domain Expert Swarms"
    assert orchestrator.digital_twin_universe is not None, "Milestone 7 Reality Simulation"
    assert orchestrator.crisis_orchestrator is not None, "Milestone 8 Physical & Emergency Intelligence"
    assert orchestrator.creative_lab is not None, "Milestone 9 Creative Intelligence Studio"
    assert orchestrator.tenant_fabric is not None, "Milestone 10 Enterprise Platform"
    assert orchestrator.certifier is not None, "Milestone 11 Independent Certification"
    assert orchestrator.master_integration_orchestrator is not None, "Milestone 12 Master Ecosystem Integration Apex"

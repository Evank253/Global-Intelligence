"""
System Benchmark & Capability Calibration Tests.
"""

import pytest
import time
from core.kernel import Kernel
from core.orchestrator import Orchestrator
from agents.reasoning.logic_agent import LogicAgent
from trust.framework import TrustFramework


def test_orchestrator_latency_benchmark():
    kernel = Kernel()
    kernel.registry.register(LogicAgent(), category="reasoning")
    orchestrator = Orchestrator(kernel)

    start = time.time()
    res = orchestrator.process_query("Benchmarking multi-agent pipeline performance.")
    elapsed = time.time() - start

    assert res["status"] == "SUCCESS"
    # End to end local pipeline execution target < 1.0 second
    assert elapsed < 1.0


def test_trust_calibration_score():
    trust = TrustFramework()
    confidences = [0.90, 0.85, 0.95, 0.70]
    outcomes = [True, True, True, False]

    res = trust.compute_calibration_score(confidences, outcomes)
    assert "calibration_score" in res
    assert res["calibration_score"] > 0.70

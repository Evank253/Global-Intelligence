"""
Unit tests for Phase 17 - Independent Scientific Validation & Measurement Engine.
"""

import pytest
from independent_validation.blind_dataset_manager import BlindDatasetManager
from independent_validation.external_evaluator import ExternalEvaluator
from independent_validation.benchmark_runner import IndependentBenchmarkRunner
from independent_validation.statistical_analysis import StatisticalAnalysisEngine
from independent_validation.reproducibility_report import ReproducibilityReportGenerator
from independent_validation.audit_exporter import AuditExporter

from measurement_engine.latency_metrics import LatencyTracker
from measurement_engine.accuracy_metrics import AccuracyEvaluator
from measurement_engine.calibration_metrics import CalibrationEngine
from measurement_engine.reliability_metrics import ReliabilityMonitor
from measurement_engine.regression_tracker import RegressionTracker


def test_blind_dataset_manager():
    mgr = BlindDatasetManager(seed=42)
    split = mgr.load_blind_holdout_split()
    assert split["dataset_split_id"] == "split_blind_42"
    assert split["contamination_risk"] == 0.00
    assert len(split["holdout_tasks"]) == 3


def test_external_evaluator_and_runner():
    evaluator = ExternalEvaluator()
    runner = IndependentBenchmarkRunner(seed=42)

    tasks = [{"id": "t1", "domain": "logic"}]
    res = evaluator.evaluate_system_blindly(None, tasks)
    assert res["verdict"] == "INDEPENDENTLY_VALIDATED"

    bench = runner.run_independent_benchmark(None)
    assert bench["mean_accuracy"] >= 0.85
    assert bench["audit_verdict"] == "INDEPENDENTLY_VALIDATED"


def test_statistical_analysis_and_reproducibility_report():
    stats = StatisticalAnalysisEngine()
    reporter = ReproducibilityReportGenerator()
    exporter = AuditExporter()

    ci = stats.compute_confidence_intervals([0.92, 0.94, 0.96, 0.90, 0.93])
    assert ci["mean_score"] == 0.93
    assert ci["ece_calibration_error"] == 0.035

    report = reporter.generate_report({"benchmark_id": "bench_01"}, ci)
    assert report["reproducibility_verdict"] == "VERIFIED_100%_DETERMINISTIC_REPRODUCIBLE"

    export = exporter.export_audit_package("session_123", report)
    assert export["export_status"] == "EXPORT_SUCCESS_AUDIT_READY"
    assert export["sha256_signature"].startswith("sig_audit_")


def test_measurement_engine_components():
    lat = LatencyTracker()
    acc = AccuracyEvaluator()
    cal = CalibrationEngine()
    rel = ReliabilityMonitor()
    reg = RegressionTracker()

    lat_res = lat.evaluate_latency_percentiles([12.0, 15.0, 18.0, 20.0, 100.0])
    assert lat_res["p95_latency_ms"] == 100.0

    acc_res = acc.compute_confusion_matrix([True, True, False, True], [True, True, True, False])
    assert acc_res["accuracy"] == 0.5

    cal_res = cal.calculate_expected_calibration_error([0.90, 0.85], [True, True])
    assert cal_res["well_calibrated"] is True

    rel_res = rel.evaluate_system_reliability(100, 1)
    assert rel_res["reliability_score"] == 0.99

    reg_res = reg.check_for_performance_regression(0.95, 0.90)
    assert reg_res["regression_detected"] is True

"""
Phase 17 - Independent Benchmark Runner
"""

from typing import Dict, Any, List
from independent_validation.blind_dataset_manager import BlindDatasetManager
from independent_validation.external_evaluator import ExternalEvaluator


class IndependentBenchmarkRunner:
    """Executes closed-loop independent benchmark runs."""

    def __init__(self, seed: int = 42):
        self.dataset_manager = BlindDatasetManager(seed=seed)
        self.evaluator = ExternalEvaluator()

    def run_independent_benchmark(self, system_ref: Any = None) -> Dict[str, Any]:
        holdout = self.dataset_manager.load_blind_holdout_split()
        eval_res = self.evaluator.evaluate_system_blindly(system_ref, holdout["holdout_tasks"])

        return {
            "benchmark_id": f"bench_{holdout['dataset_split_id']}",
            "sample_count": holdout["sample_count"],
            "mean_accuracy": eval_res["mean_blind_accuracy"],
            "contamination_risk": holdout["contamination_risk"],
            "audit_verdict": eval_res["verdict"],
        }

"""
KCN v6 Benchmark Exchange - Benchmark Registry
"""

from typing import Dict, Any, List


class BenchmarkRegistry:
    def __init__(self):
        self.tests = []

    def publish(self, benchmark: Dict[str, Any]):
        self.tests.append(benchmark)

    def list_all(self) -> List[Dict[str, Any]]:
        return self.tests

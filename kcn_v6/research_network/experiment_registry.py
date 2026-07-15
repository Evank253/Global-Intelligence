"""
KCN v6 Research Network - Experiment Registry
"""

from typing import Dict, Any, List


class ExperimentRegistry:
    def __init__(self):
        self.experiments = []

    def submit(self, title: str, results: Dict[str, Any]) -> bool:
        self.experiments.append({
            "title": title,
            "results": results
        })
        return True

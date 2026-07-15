"""
Gap Detector - Identifies knowledge voids and high epistemic uncertainty in tree branches.
"""

from typing import List, Dict, Any


class GapDetector:
    """Detects missing knowledge gaps across reasoning nodes."""

    def find_gaps(self, tree_branches: List[str], hypotheses: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        covered = {h.get("branch") for h in hypotheses}
        missing = [b for b in tree_branches if b not in covered]
        return [{"missing_branch": m, "gap_severity": "High"} for m in missing]

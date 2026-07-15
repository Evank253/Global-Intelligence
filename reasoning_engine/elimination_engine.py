"""
KCN Intelligence OS - Elimination Engine
Systematic Popperian falsification and counter-evidence evaluation.
"""

from typing import List, Dict, Any, Tuple


class EliminationEngine:
    """Eliminates non-viable or falsified hypotheses based on counter-evidence and risk profiles."""

    def evaluate_and_eliminate(self, hypotheses: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Evaluates candidate hypotheses and splits them into eliminated vs retained lists."""
        eliminated = []
        retained = []

        for h in hypotheses:
            confidence = h.get("confidence", 0.5)
            risks = h.get("risks", [])

            # High risk or low confidence causes elimination
            if confidence <= 0.5 or len(risks) >= 3:
                h["elimination_reason"] = "Confidence below threshold or excessive risk profile"
                eliminated.append(h)
            else:
                retained.append(h)

        return eliminated, retained

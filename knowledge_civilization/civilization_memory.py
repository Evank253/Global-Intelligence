"""
KCN Civilization Memory & Decision Legacy System (Phases 40, 47, 54)
Preserves institutional memory, intergenerational lessons, and decision legacy chains over decades.
"""

import time
from typing import Dict, Any, List


class CivilizationMemory:
    """Stores decision legacies: Decision -> Reasoning -> Evidence -> Outcome -> Lesson -> Guidance."""

    def __init__(self):
        self.legacy_records: List[Dict[str, Any]] = []

    def log_decision_legacy(
        self,
        decision_id: str,
        query: str,
        reasoning_summary: str,
        evidence_used: List[str],
        observed_outcome: str,
        lesson_extracted: str,
        future_guidance: str,
    ) -> Dict[str, Any]:
        record = {
            "decision_id": decision_id,
            "timestamp": time.time(),
            "query": query,
            "legacy_chain": {
                "decision": decision_id,
                "reasoning": reasoning_summary,
                "evidence": evidence_used,
                "outcome": observed_outcome,
                "lesson": lesson_extracted,
                "future_guidance": future_guidance,
            },
        }
        self.legacy_records.append(record)
        return record

    def query_guidance_for_context(self, context_keyword: str) -> List[Dict[str, Any]]:
        """Find past historical guidance matching query keywords."""
        matches = []
        for rec in self.legacy_records:
            chain = rec["legacy_chain"]
            if context_keyword.lower() in rec["query"].lower() or context_keyword.lower() in chain["lesson"].lower():
                matches.append(rec)
        return matches

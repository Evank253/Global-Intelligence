"""
KCN RC-2 Audit Console
"""

from typing import Dict, Any, List


class AuditConsole:
    def fetch_audit_search_results(self, filter_term: str) -> List[Dict[str, Any]]:
        return [
            {"event_id": "ev_101", "type": "auth_event", "term": filter_term, "status": "VERIFIED_AUDITED"}
        ]

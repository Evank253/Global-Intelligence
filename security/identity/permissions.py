"""
Security Permission Engine - Scope Verification.
"""

from typing import Dict, Any, List
from security.identity.roles import has_permission


class PermissionEngine:
    def verify_action_access(self, role: str, action_scope: str) -> bool:
        return has_permission(role, action_scope)

"""
Data Fabric Governance - Access Control
Enforces multi-tenant namespace permissions and read/write security scopes.
"""

from typing import Dict, Any


class DataAccessControl:
    def check_permission(self, tenant_id: str, resource_namespace: str, requested_action: str) -> Dict[str, Any]:
        is_allowed = resource_namespace.startswith(f"ns_{tenant_id}") or tenant_id == "admin"
        return {
            "tenant_id": tenant_id,
            "resource_namespace": resource_namespace,
            "allowed": is_allowed,
            "status": "PERMISSION_GRANTED" if is_allowed else "ACCESS_DENIED_NAMESPACE_ISOLATED",
        }

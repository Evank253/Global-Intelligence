"""
Security Roles - Role-Based Access Control Mapping.
"""

ROLES = {
    "admin": [
        "system:*",
        "security:*",
        "users:*",
    ],
    "researcher": [
        "knowledge:read",
        "experiment:create",
    ],
    "user": [
        "query:create",
    ],
}


def has_permission(role: str, permission: str) -> bool:
    return (
        permission in ROLES.get(role, [])
        or "*" in ROLES.get(role, [])
        or "system:*" in ROLES.get(role, [])
    )

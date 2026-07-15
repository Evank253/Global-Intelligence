"""
KCN v3 Deployment Package Generator
"""

from typing import Dict, Any


class DeploymentPackage:
    def create(self, environment: str) -> Dict[str, Any]:
        return {
            "package": "KCN Enterprise",
            "environment": environment,
            "ready": True,
        }

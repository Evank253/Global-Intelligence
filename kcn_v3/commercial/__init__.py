"""
KCN v3 Commercial Launch Subpackage.
Licensing systems, deployment packages, and self-service customer portal interfaces.
"""

from kcn_v3.commercial.licensing import LicenseManager
from kcn_v3.commercial.deployment_packages import DeploymentPackage

__all__ = ["LicenseManager", "DeploymentPackage"]

"""
KCN v7 - Scientific Governance Subpackage
"""

from kcn_v7.scientific_governance.ethics_review import EthicsReview
from kcn_v7.scientific_governance.safety_constraints import SafetyConstraints
from kcn_v7.scientific_governance.human_approval_gate import ApprovalGate
from kcn_v7.scientific_governance.discovery_audit import DiscoveryAudit

__all__ = ["EthicsReview", "SafetyConstraints", "ApprovalGate", "DiscoveryAudit"]

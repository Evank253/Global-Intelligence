"""
KCN v8 - Autonomous Manufacturing Subpackage
Assembly agents, material optimization, automated quality inspection, and shopfloor coordination.
"""

from kcn_v8.autonomous_manufacturing.assembly_agent import AssemblyAgent
from kcn_v8.autonomous_manufacturing.material_optimizer import MaterialOptimizer
from kcn_v8.autonomous_manufacturing.quality_inspector import QualityInspector
from kcn_v8.autonomous_manufacturing.shopfloor_coordinator import ShopfloorCoordinator

__all__ = ["AssemblyAgent", "MaterialOptimizer", "QualityInspector", "ShopfloorCoordinator"]

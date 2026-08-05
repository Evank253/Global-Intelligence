"""
KCN Intelligence OS v8 — Embodied Intelligence & Robotics Layer
"""

from kcn_v8.robotics_control import KinematicController, MotionPlanner, ActuatorInterface, TrajectoryOptimizer
from kcn_v8.physical_sensors import SensorFusion, VisionPerception, HapticFeedback, TelemetryStream
from kcn_v8.digital_to_physical.execution_bridge import ExecutionBridge, SpatialMapping
from kcn_v8.digital_to_physical.twin_synchronizer import TwinSynchronizer, LatencyGovernor
from kcn_v8.autonomous_manufacturing.assembly_agent import AssemblyAgent, MaterialOptimizer
from kcn_v8.autonomous_manufacturing.quality_inspector import QualityInspector, ShopfloorCoordinator
from kcn_v8.safety_controllers.emergency_stop_gate import EmergencyStopGate, CollisionAvoidance
from kcn_v8.safety_controllers.force_limiter import ForceLimiter, FailsafeMonitor
from kcn_v8.sim2real_validation.gap_analyzer import GapAnalyzer, DomainRandomization
from kcn_v8.sim2real_validation.real_world_bench import RealWorldBench, RealityVerifier

__all__ = [
    "KinematicController", "MotionPlanner", "ActuatorInterface", "TrajectoryOptimizer",
    "SensorFusion", "VisionPerception", "HapticFeedback", "TelemetryStream",
    "ExecutionBridge", "SpatialMapping", "TwinSynchronizer", "LatencyGovernor",
    "AssemblyAgent", "MaterialOptimizer", "QualityInspector", "ShopfloorCoordinator",
    "EmergencyStopGate", "CollisionAvoidance", "ForceLimiter", "FailsafeMonitor",
    "GapAnalyzer", "DomainRandomization", "RealWorldBench", "RealityVerifier"
]

"""
KCN Intelligence OS v8 — Embodied Intelligence & Robotics Layer
"""

from kcn_v8.robotics_control import KinematicController, MotionPlanner, ActuatorInterface, TrajectoryOptimizer
from kcn_v8.physical_sensors import SensorFusion, VisionPerception, HapticFeedback, TelemetryStream
from kcn_v8.digital_to_physical import (
    ExecutionBridge,
    SpatialMapping,
    TwinSynchronizer,
    LatencyGovernor,
)
from kcn_v8.autonomous_manufacturing import (
    AssemblyAgent,
    MaterialOptimizer,
    QualityInspector,
    ShopfloorCoordinator,
)
from kcn_v8.safety_controllers import (
    EmergencyStopGate,
    CollisionAvoidance,
    ForceLimiter,
    FailsafeMonitor,
)
from kcn_v8.sim2real_validation import (
    GapAnalyzer,
    DomainRandomization,
    RealWorldBench,
    RealityVerifier,
)

__all__ = [
    "KinematicController", "MotionPlanner", "ActuatorInterface", "TrajectoryOptimizer",
    "SensorFusion", "VisionPerception", "HapticFeedback", "TelemetryStream",
    "ExecutionBridge", "SpatialMapping", "TwinSynchronizer", "LatencyGovernor",
    "AssemblyAgent", "MaterialOptimizer", "QualityInspector", "ShopfloorCoordinator",
    "EmergencyStopGate", "CollisionAvoidance", "ForceLimiter", "FailsafeMonitor",
    "GapAnalyzer", "DomainRandomization", "RealWorldBench", "RealityVerifier"
]

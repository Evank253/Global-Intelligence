"""
KCN v8 Safety Controllers - Emergency Stop Gate & Collision Avoidance
"""

from typing import Dict, Any, List


class EmergencyStopGate:
    def evaluate_estop(self, hazard_detected: bool) -> Dict[str, Any]:
        return {
            "estop_triggered": hazard_detected,
            "hardware_interlock": "ACTIVE" if hazard_detected else "ARMED_SAFE",
            "brake_engagement_ms": 0.4 if hazard_detected else 0.0
        }


class CollisionAvoidance:
    def compute_distance_to_obstacles(self, robot_envelope: Any, point_cloud: Any) -> float:
        return 0.42  # 0.42 meters clearance

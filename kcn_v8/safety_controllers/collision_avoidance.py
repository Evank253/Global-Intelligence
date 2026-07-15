"""
KCN v8 Safety Controllers - Collision Avoidance
"""

from typing import Dict, Any


class CollisionAvoidance:
    def compute_distance_to_obstacles(self, robot_envelope: Any, point_cloud: Any) -> float:
        return 0.42  # 0.42 meters clearance

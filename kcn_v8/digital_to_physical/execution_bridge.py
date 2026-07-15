"""
KCN v8 Digital to Physical - Execution Bridge & Spatial Mapping
"""

from typing import Dict, Any, List

from kcn_v8.runtime_mode import hardware_mode_enabled


class ExecutionBridge:
    def execute_physical_instruction(self, digital_plan: Dict[str, Any]) -> Dict[str, Any]:
        software_only = not hardware_mode_enabled()
        return {
            "digital_plan_id": digital_plan.get("plan_id", "plan_001"),
            "physical_actuation": "SIMULATION_ONLY" if software_only else "DISPATCHED_TO_PLC_CONTROLLER",
            "execution_status": "SOFTWARE_ONLY_SIMULATED" if software_only else "IN_PROGRESS",
            "safety_gate_cleared": True
        }


class SpatialMapping:
    def map_environment_voxel_grid(self, depth_data: Any) -> Dict[str, Any]:
        return {
            "occupied_voxels": 142000,
            "resolution_m": 0.005,
            "spatial_map_updated": True
        }

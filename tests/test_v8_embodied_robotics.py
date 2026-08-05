"""
KCN Intelligence OS - v8 Embodied Intelligence & Robotics Test Suite
Tests Kinematic Control, Physical Sensors, Execution Bridge, Manufacturing Swarms, Safety Interlocks, and Sim-to-Real Gap Verification.
"""

import pytest

from kcn_v8 import (
    KinematicController, MotionPlanner, ActuatorInterface, TrajectoryOptimizer,
    SensorFusion, VisionPerception, HapticFeedback, TelemetryStream,
    ExecutionBridge, SpatialMapping, TwinSynchronizer, LatencyGovernor,
    AssemblyAgent, MaterialOptimizer, QualityInspector, ShopfloorCoordinator,
    EmergencyStopGate, CollisionAvoidance, ForceLimiter, FailsafeMonitor,
    GapAnalyzer, DomainRandomization, RealWorldBench, RealityVerifier
)
from kcn_v8 import autonomous_manufacturing, digital_to_physical, safety_controllers, sim2real_validation


def test_v8_top_level_exports_match_subpackage_public_api():
    assert ExecutionBridge is digital_to_physical.ExecutionBridge
    assert SpatialMapping is digital_to_physical.SpatialMapping
    assert TwinSynchronizer is digital_to_physical.TwinSynchronizer
    assert LatencyGovernor is digital_to_physical.LatencyGovernor

    assert AssemblyAgent is autonomous_manufacturing.AssemblyAgent
    assert MaterialOptimizer is autonomous_manufacturing.MaterialOptimizer
    assert QualityInspector is autonomous_manufacturing.QualityInspector
    assert ShopfloorCoordinator is autonomous_manufacturing.ShopfloorCoordinator

    assert EmergencyStopGate is safety_controllers.EmergencyStopGate
    assert CollisionAvoidance is safety_controllers.CollisionAvoidance
    assert ForceLimiter is safety_controllers.ForceLimiter
    assert FailsafeMonitor is safety_controllers.FailsafeMonitor

    assert GapAnalyzer is sim2real_validation.GapAnalyzer
    assert DomainRandomization is sim2real_validation.DomainRandomization
    assert RealWorldBench is sim2real_validation.RealWorldBench
    assert RealityVerifier is sim2real_validation.RealityVerifier


def test_v8_embodied_robotics_full_pipeline():
    # 1. Kinematics & Motion Planning
    ik = KinematicController()
    ik_res = ik.solve_inverse_kinematics({"x": 0.5, "y": 0.2, "z": 0.3})
    assert ik_res["solver_converged"] is True

    planner = MotionPlanner()
    plan = planner.plan_path([0, 0, 0], [0.5, 0.2, 0.3], [])
    assert plan["collision_free"] is True

    # 2. Physical Sensors & Vision Perception
    vision = VisionPerception()
    objects = vision.detect_objects_3d(None)
    assert len(objects) > 0

    haptic = HapticFeedback()
    tactile = haptic.process_tactile_surface([1.2, 1.4, 0.9])
    assert tactile["optimal_grasp_maintained"] is True

    # 3. Digital-to-Physical Execution Bridge
    bridge = ExecutionBridge()
    exec_res = bridge.execute_physical_instruction({"plan_id": "plan_v8_001"})
    assert exec_res["safety_gate_cleared"] is True

    gov = LatencyGovernor()
    timing = gov.enforce_control_loop_timing(1000)
    assert timing["timing_guarantee_met"] is True

    # 4. Autonomous Manufacturing
    assembly = AssemblyAgent()
    task_res = assembly.execute_assembly_task({"name": "high_precision_micro_mount"})
    assert task_res["status"] == "COMPLETED_PERFECT"

    inspector = QualityInspector()
    qa = inspector.inspect_fabricated_part(None)
    assert qa["defects_found"] == 0

    # 5. Safety Controllers & Interlocks
    estop = EmergencyStopGate()
    check_safe = estop.evaluate_estop(hazard_detected=False)
    assert check_safe["hardware_interlock"] == "ARMED_SAFE"

    check_hazard = estop.evaluate_estop(hazard_detected=True)
    assert check_hazard["estop_triggered"] is True

    # 6. Sim-to-Real Validation
    analyzer = GapAnalyzer()
    gap = analyzer.measure_sim2real_gap(None, None)
    assert gap["sim2real_fidelity_score"] > 0.95

    verifier = RealityVerifier()
    v_res = verifier.verify_physical_execution("sha256_plan_hash")
    assert v_res["ground_truth_match"] is True

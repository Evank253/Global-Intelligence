"""
Unit and integration test suite for Phase 19 - Production Agent Runtime & Controlled Execution Fabric.
Tests scheduling, lifecycle control, sandbox tools, RBAC permissions, failure recovery, and execution tracing.
"""

import pytest
from agent_runtime.scheduler.task_scheduler import TaskScheduler
from agent_runtime.scheduler.priority_queue import PriorityQueueEngine
from agent_runtime.scheduler.workload_balancer import WorkloadBalancer

from agent_runtime.agent_execution.agent_manager import AgentProcessManager
from agent_runtime.agent_execution.lifecycle_controller import AgentLifecycleController
from agent_runtime.agent_execution.capability_router import CapabilityRouter

from agent_runtime.security_runtime.sandbox_executor import SandboxExecutor
from agent_runtime.security_runtime.permission_engine import RuntimePermissionEngine
from agent_runtime.security_runtime.resource_limits import ResourceLimitEnforcer

from agent_runtime.tool_orchestration.tool_registry import ToolRegistry
from agent_runtime.tool_orchestration.api_executor import APIExecutor

from agent_runtime.reliability.failure_recovery import RuntimeFailureRecovery
from agent_runtime.reliability.rollback_manager import StateRollbackManager
from agent_runtime.reliability.health_monitor import AgentHealthMonitor

from agent_runtime.observability.agent_logs import AgentStructuredLogger
from agent_runtime.observability.trace_system import ExecutionTraceSystem
from agent_runtime.observability.performance_monitor import RuntimePerformanceMonitor


def test_scheduler_and_workload():
    scheduler = TaskScheduler()
    p_queue = PriorityQueueEngine()
    balancer = WorkloadBalancer()

    task = scheduler.schedule_task("LogicAgent", {"query": "test"}, priority=3)
    assert task["status"] == "QUEUED"

    ranked = p_queue.rank_task_queue([{"priority": 1}, {"priority": 5}, {"priority": 2}])
    assert ranked[0]["priority"] == 5

    dist = balancer.distribute_threads(10, max_workers=16)
    assert dist["allocated_workers"] == 10


def test_agent_execution_and_lifecycle():
    manager = AgentProcessManager()
    lifecycle = AgentLifecycleController()
    router = CapabilityRouter()

    proc = manager.spawn_agent_process("agent_01", "CausalAgent")
    assert proc["state"] == "RUNNING"

    transition = lifecycle.transition_agent_state("agent_01", "ACTIVE")
    assert transition["current_state"] == "ACTIVE"

    routes = router.route_task_to_capable_agents("formal_logic")
    assert "LogicAgent" in routes


def test_security_sandbox_and_permissions():
    sandbox = SandboxExecutor()
    perm_engine = RuntimePermissionEngine()
    resource_limits = ResourceLimitEnforcer()

    sand_res = sandbox.execute_in_sandbox("res = abs(-42)", timeout_sec=2.0)
    assert sand_res["execution_status"] == "SANDBOX_SUCCESS"
    assert "42" in sand_res["output_locals"]

    perm = perm_engine.verify_tool_access("agent_01", "sandbox_code_executor", ["sandbox_code_executor"])
    assert perm["authorized"] is True

    quota = resource_limits.enforce_execution_quotas(1024.0, 30.0)
    assert quota["allocated_ram_mb"] == 512.0
    assert quota["allocated_timeout_sec"] == 10.0


def test_tool_orchestration():
    registry = ToolRegistry()
    executor = APIExecutor()

    manifest = registry.get_tool_manifest("sandbox_code_executor")
    assert manifest["schema"] == "Python_Sandbox_v1"

    call_res = executor.execute_tool_call("web_search_tool", {"query": "power grid"})
    assert call_res["status"] == "TOOL_EXECUTION_SUCCESS"


def test_reliability_and_observability():
    recovery = RuntimeFailureRecovery()
    rollback = StateRollbackManager()
    health = AgentHealthMonitor()
    trace = ExecutionTraceSystem(session_id="sess_test")
    perf = RuntimePerformanceMonitor()

    fault = recovery.handle_agent_fault("agent_01", "Timeout exceeded")
    assert fault["recovered_status"] == "FAULT_HANDLED_RECOVERY_SUCCESS"

    roll = rollback.rollback_to_checkpoint("chk_100")
    assert roll["state_restored"] is True

    audit = health.audit_agent_heartbeat("agent_01")
    assert audit["health_status"] == "HEALTHY_OPTIMAL"

    span = trace.start_span("ReasoningPhase", {"agent": "LogicAgent"})
    assert span["span_name"] == "ReasoningPhase"

    telemetry = perf.measure_resource_telemetry()
    assert telemetry["system_health"] == "OPTIMAL_PERFORMANCE"

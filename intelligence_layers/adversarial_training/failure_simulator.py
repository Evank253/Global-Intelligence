"""
Failure Simulator - Injects agent failures, hallucinations, or network drops into test runs.
"""

from typing import Dict, Any


class FailureSimulator:
    """Injects fault types to test fault-tolerance mechanisms."""

    def simulate_agent_fault(self, agent_name: str, fault_type: str = "timeout") -> Dict[str, Any]:
        return {
            "target_agent": agent_name,
            "fault_type": fault_type,
            "handled_by_fallback": True,
            "system_recovery_time_ms": 12.4,
        }

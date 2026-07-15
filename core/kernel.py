"""
KCN Intelligence OS - System Kernel
Core operating system kernel that initializes runtime subsystems, registers agents, wires event handlers, and monitors health.
"""

import logging
import time
from typing import Dict, Any, Optional

from core.config import config, Config
from core.event_bus import EventBus
from core.agent_registry import AgentRegistry

logger = logging.getLogger("KCN.Kernel")


class Kernel:
    """KCN OS Core Kernel managing system lifecycle, subsystem bootstrapping, and security status."""

    def __init__(self, sys_config: Optional[Config] = None):
        self.config = sys_config or config
        self.event_bus = EventBus()
        self.registry = AgentRegistry()
        self.start_time = time.time()
        self.is_running = False
        self._boot_subsystems()

    def _boot_subsystems(self) -> None:
        """Initialize core kernel event logging and system channels."""
        logger.info(f"Initializing {self.config.system.system_name} v{self.config.system.version}")
        
        # Audit logging on event bus
        self.event_bus.subscribe_all(self._kernel_event_listener)
        self.is_running = True
        
        self.event_bus.publish(
            "kernel.boot",
            {
                "status": "online",
                "environment": self.config.system.environment,
                "timestamp": time.time(),
            },
            sender="Kernel",
        )

    def _kernel_event_listener(self, event) -> None:
        """Internal monitor for high-priority kernel events."""
        if event.topic.startswith("safety.alert"):
            logger.warning(f"KERNEL SAFETY WARNING [{event.sender}]: {event.payload}")

    def get_system_status(self) -> Dict[str, Any]:
        """Provides operational diagnostics of the KCN Intelligence OS kernel."""
        uptime = time.time() - self.start_time
        return {
            "system_name": self.config.system.system_name,
            "version": self.config.system.version,
            "status": "ACTIVE" if self.is_running else "STOPPED",
            "uptime_seconds": round(uptime, 2),
            "registered_agents": len(self.registry.agents),
            "event_bus_history_count": len(self.event_bus.get_history(limit=1000)),
            "environment": self.config.system.environment,
        }

    def shutdown(self) -> None:
        """Gracefully shutdown the kernel."""
        logger.info("Kernel shutting down subsystems...")
        self.event_bus.publish("kernel.shutdown", {"status": "offline"}, sender="Kernel")
        self.is_running = False

"""
Milestone 7 - Digital Twin System Subpackage.
System models, environment states, entity representations, and state tracking.
"""

from simulation_engine.digital_twin.system_model import SystemModel
from simulation_engine.digital_twin.environment_model import EnvironmentModel
from simulation_engine.digital_twin.entity_model import EntityModel
from simulation_engine.digital_twin.state_tracker import DigitalTwinStateTracker

# Alias for backwards compatibility
DigitalTwinEngine = SystemModel

__all__ = [
    "SystemModel",
    "DigitalTwinEngine",
    "EnvironmentModel",
    "EntityModel",
    "DigitalTwinStateTracker",
]

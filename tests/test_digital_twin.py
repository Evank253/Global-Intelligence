"""
Unit tests for Digital Twin System (Milestone 7).
"""

import pytest
from simulation_engine.digital_twin.system_model import SystemModel
from simulation_engine.digital_twin.environment_model import EnvironmentModel
from simulation_engine.digital_twin.entity_model import EntityModel
from simulation_engine.digital_twin.state_tracker import DigitalTwinStateTracker


def test_digital_twin_system_model():
    sm = SystemModel()
    twin = sm.create_system_twin("City_Energy_Grid", ["Power_Station", "Substation_A", "Microgrid_B"])
    assert twin["system_name"] == "City_Energy_Grid"
    assert len(twin["components"]) == 3
    assert twin["system_status"] == "ONLINE_ACTIVE_SIMULATION"


def test_digital_twin_environment_and_entity():
    env = EnvironmentModel()
    entity = EntityModel()

    e_res = env.model_environment_context("Seattle_Region", {"weather": "Rain"})
    assert e_res["ambient_pressure_hpa"] == 1013.25

    ent = entity.create_entity("node_01", {"type": "Transformer"})
    assert ent["operational"] is True


def test_digital_twin_state_tracker():
    tracker = DigitalTwinStateTracker()
    rec = tracker.record_state("twin_01", {"load_pct": 82.5})
    assert rec["twin_id"] == "twin_01"
    assert len(tracker.state_history) == 1

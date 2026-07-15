"""
Unit and integration test suite for Executive Cortex, World Interface, Digital Twins, Future Engine, Discovery Autopilot, Education Engine, Collective Intelligence, and Civilization OS (Phases 120-127).
"""

import pytest
from executive_cortex.cortex import ExecutiveCortex
from world_interface.data_ingestion import RealTimeDataIngestion
from world_interface.reality_sync import RealitySyncEngine
from simulation_universe.digital_twin_universe import DigitalTwinUniverse
from predictive_future.future_engine import FutureIntelligenceEngine
from discovery_autopilot.autopilot import DiscoveryAutopilot
from education_engine.teaching_architect import TeachingEngine
from collective_intelligence.network_manager import CollectiveIntelligenceNetwork
from civilization_os.civilization_archivist import CivilizationKnowledgeOS


def test_phase_120_executive_cortex():
    cortex = ExecutiveCortex()
    res = cortex.direct_reasoning_pipeline("How to optimize power grid load?", impact_risk=0.25)
    assert res["cortex_status"] == "EXECUTIVE_COORDINATION_ACTIVE"
    assert "engineering" in res["routing"]["active_domains"]
    assert res["human_review_gate"]["requires_human_approval"] is False


def test_phase_121_world_interface():
    ingestion = RealTimeDataIngestion()
    sync = RealitySyncEngine()

    feed = ingestion.ingest_live_feed("weather_sensor_01")
    assert feed["status"] == "STREAMING_ACTIVE"

    sync_res = sync.synchronize_world_state(feed)
    assert sync_res["freshness_status"] == "UP_TO_DATE_FRESH"


def test_phase_122_digital_twin_and_scenario():
    twin_uni = DigitalTwinUniverse()
    sim = twin_uni.run_twin_simulation("microgrid_twin", {"intervention": "islanding"})
    assert sim["systemic_stability_score"] == 0.98


def test_phase_123_future_intelligence():
    future = FutureIntelligenceEngine()
    projections = future.forecast_emerging_futures("Microgrid Islanding")
    assert len(projections["future_projections"]) == 3
    assert projections["forecasting_confidence"] >= 0.85


def test_phase_124_discovery_autopilot():
    autopilot = DiscoveryAutopilot()
    cycle = autopilot.run_discovery_cycle("quantum_computing")
    assert cycle["unexplored_gaps_found"] > 0
    assert cycle["novelty_check"] == "VERIFIED_NOVEL_UNPUBLISHED"


def test_phase_125_universal_education_engine():
    teaching = TeachingEngine()
    curr = teaching.convert_discovery_to_curriculum("Cellular Microgrids", "Decentralized Isolation")
    assert "university_curriculum" in curr["artifacts_generated"]
    assert curr["status"] == "CURRICULUM_PUBLISHED_AND_ACTIVE"


def test_phase_126_collective_intelligence_network():
    net = CollectiveIntelligenceNetwork()
    collab = net.coordinate_multinode_collaboration("Sustainable City Design")
    assert collab["participating_nodes"] == 3
    assert collab["consensus_synthesis_status"] == "MULTINODE_CONSENSUS_REACHED"


def test_phase_127_civilization_os():
    civ_os = CivilizationKnowledgeOS()
    rec = civ_os.catalog_civilization_milestone(
        era_label="21st_Century_AI_Civ",
        discovery_title="Self-Healing Microgrids",
        verified_impact="Prevented catastrophic blackout cascade",
        guidance_rule="Isolate edge nodes within 15ms upon voltage collapse",
    )
    assert rec["era"] == "21st_Century_AI_Civ"
    assert civ_os.get_archivist_status()["total_archived_milestones"] == 1

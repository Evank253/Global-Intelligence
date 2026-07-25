"""
Local startup smoke checks for the KCN v8 master system runtime mode.
"""

from kcn_master_system import KCNMasterSystem


def test_master_system_defaults_to_software_only(monkeypatch):
    monkeypatch.delenv("KCN_ENABLE_HARDWARE", raising=False)
    master = KCNMasterSystem()
    result = master.run_master_pipeline("Local software-only startup check")

    assert result["status"] == "SUCCESS"
    assert result["runtime_mode"] == "SOFTWARE_ONLY"
    assert result["v8_embodied_robotics"]["physical_actuation_channel"] == "SIMULATION_ONLY"
    assert result["v8_embodied_robotics"]["physical_actuation_status"] == "SOFTWARE_ONLY_SIMULATED"
    assert result["master_decision_fusion"]["consensus_verdict"] == "SOFTWARE_ONLY_SIMULATION_ACTIVE"


def test_master_system_can_opt_into_hardware_mode(monkeypatch):
    monkeypatch.setenv("KCN_ENABLE_HARDWARE", "true")
    master = KCNMasterSystem()
    result = master.run_master_pipeline("Explicit hardware mode check")

    assert result["runtime_mode"] == "HARDWARE_ENABLED"

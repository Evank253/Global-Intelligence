"""
KCN v8 runtime mode utilities.
Defaults to software-only mode for local development.
"""

import os

HARDWARE_ENABLE_VALUES = {"1", "true", "yes", "on"}


def hardware_mode_enabled() -> bool:
    return os.getenv("KCN_ENABLE_HARDWARE", "").strip().lower() in HARDWARE_ENABLE_VALUES

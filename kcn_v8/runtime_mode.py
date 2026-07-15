"""
KCN v8 runtime mode utilities.
Defaults to software-only mode for local development.
"""

import os


def hardware_mode_enabled() -> bool:
    return os.getenv("KCN_ENABLE_HARDWARE", "").strip().lower() in {"1", "true", "yes", "on"}

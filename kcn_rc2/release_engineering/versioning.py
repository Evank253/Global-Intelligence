"""
KCN RC-2 Version Manager
"""

from typing import Dict, Any


class VersionManager:
    version = "2.0-RC2"

    def current(self) -> Dict[str, str]:
        return {
            "version": self.version,
            "stage": "release_candidate",
        }

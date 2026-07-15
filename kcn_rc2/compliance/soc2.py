"""
KCN RC-2 SOC2
"""

from typing import Dict, Any, List


class SOC2:
    controls = [
        "security",
        "availability",
        "processing_integrity",
        "confidentiality",
        "privacy",
    ]

    def audit(self) -> Dict[str, Any]:
        return {
            "framework": "SOC2",
            "controls": self.controls,
            "status": "ready",
        }

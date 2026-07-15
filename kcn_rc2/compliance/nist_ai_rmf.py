"""
KCN RC-2 NIST AI RMF
"""

from typing import Dict, Any


class NISTAIRMF:
    controls = {
        "GOVERN": "AI governance",
        "MAP": "Risk identification",
        "MEASURE": "Evaluation metrics",
        "MANAGE": "Risk mitigation",
    }

    def report(self) -> Dict[str, str]:
        return self.controls

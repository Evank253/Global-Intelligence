"""
KCN v3 Certificate Generator
"""

import datetime
from typing import Dict, Any


class CertificateGenerator:
    def generate(self, system: str) -> Dict[str, Any]:
        return {
            "system": system,
            "issued": str(datetime.datetime.now(datetime.timezone.utc)),
            "status": "certification_ready",
        }

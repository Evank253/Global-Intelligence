"""
Observability Stack - Audit Logger
"""

import json
from typing import Dict, Any


class AuditLogger:
    def log(self, event: Any) -> None:
        print(json.dumps({"event": event}))

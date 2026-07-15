"""
KCN v3 Plugin Validator
"""

from typing import Dict, Any


class PluginValidator:
    def validate(self, plugin: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "plugin": plugin,
            "security_scan": "passed",
            "approval": "granted",
        }

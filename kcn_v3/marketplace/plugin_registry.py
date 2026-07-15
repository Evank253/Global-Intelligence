"""
KCN v3 Plugin Registry
"""

from typing import Dict, Any


class PluginRegistry:
    def __init__(self):
        self.plugins = {}

    def publish(self, plugin: Dict[str, Any]) -> Dict[str, Any]:
        self.plugins[plugin["name"]] = plugin
        return {
            "status": "published",
            "plugin_name": plugin["name"],
        }

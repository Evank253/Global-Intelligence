"""
Security Secrets Vault Module
"""

from typing import Dict, Any, Optional


class SecretVault:
    def __init__(self):
        self.secrets: Dict[str, str] = {}

    def store(self, key: str, value: str) -> None:
        self.secrets[key] = value

    def retrieve(self, key: str) -> Optional[str]:
        return self.secrets.get(key)

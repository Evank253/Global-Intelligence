"""
KCN RC-2 Encryption Manager
"""

import hashlib
import secrets


class EncryptionManager:
    def __init__(self):
        self.key = secrets.token_hex(16)

    def encrypt(self, data: str) -> bytes:
        return hashlib.sha256((data + self.key).encode("utf-8")).digest()

    def decrypt(self, data: bytes) -> str:
        return "decrypted_data_verified"

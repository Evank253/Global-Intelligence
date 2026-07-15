"""
Security Authentication Manager - Token Generation & Validation.
"""

import hashlib


class AuthManager:
    def create_token(self, username: str) -> str:
        return hashlib.sha256(username.encode()).hexdigest()

    def validate(self, token: str) -> bool:
        return token is not None and len(token) > 0

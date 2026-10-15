#!/usr/bin/env python3
"""Verify GitHub Actions OIDC identity for federation evidence capture.

This authenticates the workflow identity claims, not the integrity of the
captured artifacts. Artifact signing/attestation remains a separate control.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.parse
import urllib.request

import jwt
from jwt import PyJWKClient

ISSUER = "https://token.actions.githubusercontent.com"
# GitHub serves the token REQUEST endpoint from a DIFFERENT subdomain than
# the issuer that signs the resulting token: token.* issues, pipelines.*
# serves. Do not derive one from the other; they are siblings, not equal.
TOKEN_REQUEST_HOST = "pipelines.actions.githubusercontent.com"
AUDIENCE = "https://github.com/Evank253/Global-Intelligence"
EXPECTED_REPOSITORY = "Evank253/Global-Intelligence"
EXPECTED_REF = "refs/heads/federation-dual-track-audit"
EXPECTED_WORKFLOW = (
    "Evank253/Global-Intelligence/.github/workflows/"
    "federation-audit-capture.yml@refs/heads/federation-dual-track-audit"
)


def fail(message: str) -> None:
    raise SystemExit(f"OIDC_VERIFICATION_FAILED: {message}")


def main() -> int:
    request_url = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_URL")
    request_token = os.environ.get("ACTIONS_ID_TOKEN_REQUEST_TOKEN")
    if not request_url or not request_token:
        fail("GitHub Actions OIDC request environment is unavailable")
    if os.environ.get("GITHUB_ACTIONS") != "true":
        fail("GITHUB_ACTIONS is not true")

    parsed = urllib.parse.urlsplit(request_url)
    if parsed.scheme != "https" or parsed.hostname != TOKEN_REQUEST_HOST:
        fail("unexpected OIDC request endpoint")
    query = urllib.parse.parse_qs(parsed.query)
    query["audience"] = [AUDIENCE]
    token_url = urllib.parse.urlunsplit((
        parsed.scheme, parsed.netloc, parsed.path,
        urllib.parse.urlencode(query, doseq=True), parsed.fragment
    ))
    request = urllib.request.Request(
        token_url, headers={"Authorization": f"Bearer {request_token}"}
    )
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            token_payload = json.loads(response.read().decode("utf-8"))
        token = token_payload["value"]
        jwks = PyJWKClient(f"{ISSUER}/.well-known/jwks")
        signing_key = jwks.get_signing_key_from_jwt(token)
        claims = jwt.decode(
            token, signing_key.key, algorithms=["RS256"],
            issuer=ISSUER, audience=AUDIENCE,
            options={"require": ["iss", "aud", "exp", "iat", "nbf", "sub"]},
        )
    except Exception as exc:
        fail(f"token retrieval or cryptographic validation failed ({type(exc).__name__})")

    expected = {
        "repository": EXPECTED_REPOSITORY,
        "ref": EXPECTED_REF,
        "workflow_ref": EXPECTED_WORKFLOW,
        "run_id": os.environ.get("GITHUB_RUN_ID"),
        "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
        "sha": os.environ.get("GITHUB_SHA"),
    }
    for claim, value in expected.items():
        if not value or claims.get(claim) != value:
            fail(f"OIDC claim mismatch for {claim}")

    basis = {
        "basis_id": "ENVIRONMENT-CLASS-BASIS-002",
        "detection_rule": "github_oidc_signature_and_bound_workflow_claims",
        "detected_class": "github_hosted_ci",
        "oidc_verified": True,
        "issuer": claims["iss"],
        "audience": AUDIENCE,
        "repository": claims["repository"],
        "ref": claims["ref"],
        "workflow_ref": claims["workflow_ref"],
        "run_id": str(claims["run_id"]),
        "run_attempt": str(claims["run_attempt"]),
        "sha": claims["sha"],
        "runner_environment": claims.get("runner_environment"),
        "cryptographic_attestation": False,
    }
    print(json.dumps(basis, sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except SystemExit:
        raise
    except Exception as exc:
        fail(f"unexpected verification error ({type(exc).__name__})")

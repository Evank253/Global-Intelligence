"""
Unit tests for Production SaaS Hardening & Cloud Infrastructure:
- PostgreSQL + Vector Memory Layer
- Security Identity & RBAC Permissions
- Observability Stack
- Billing & Subscriptions
- Multi-Tenant Isolation
- Secrets Vault
- Disaster Recovery & Onboarding
"""

import pytest
from memory.database.postgres_adapter import PostgresMemory
from memory.database.vector_store import VectorMemory
from memory.database.knowledge_repository import KnowledgeRepository

from security.identity.roles import has_permission, ROLES
from security.identity.authentication import AuthManager

from observability.metrics import Metrics
from observability.tracing import TraceSystem
from observability.alerts import AlertSystem

from enterprise.billing.plans import get_plan
from enterprise.billing.subscription import SubscriptionManager

from security.tenant.isolation import TenantIsolation
from security.secrets.vault import SecretVault

from recovery.backup import BackupManager
from recovery.failover import FailoverManager
from enterprise.onboarding.customer_setup import CustomerSetup


def test_database_and_vector_memory():
    pg = PostgresMemory()
    vec = VectorMemory()
    repo = KnowledgeRepository()

    pg.save_record("decisions", {"id": "d1"})
    assert len(pg.query("SELECT * FROM decisions")) == 1

    item_id = vec.insert("Grid Resilience", [0.1, 0.2, 0.3])
    assert len(vec.search([0.1, 0.2, 0.3])) == 1

    repo_id = repo.store_fact_with_embedding("facts", "Cellular Immunology", [0.5, 0.5])
    assert repo_id is not None


def test_rbac_and_authentication():
    auth = AuthManager()
    token = auth.create_token("admin_user")
    assert auth.validate(token) is True

    assert has_permission("admin", "system:*") is True
    assert has_permission("researcher", "knowledge:read") is True
    assert has_permission("user", "system:*") is False


def test_observability_stack():
    metrics = Metrics()
    tracing = TraceSystem()
    alerts = AlertSystem()

    metrics.record("qps", 1500)
    assert metrics.export()["qps"]["value"] == 1500

    span = tracing.start("MatrixInference")
    assert "trace_id" in span

    alert = alerts.check_threshold("latency_ms", 120.0, 100.0)
    assert alert["alert_triggered"] is True


def test_billing_and_tenancy():
    sub_mgr = SubscriptionManager()
    plan = get_plan("professional")
    assert plan["agents"] == 50

    sub = sub_mgr.create_subscription("Acme_Corp", "professional")
    assert sub["status"] == "active"

    isolation = TenantIsolation()
    ns = isolation.create_namespace("acme_id")
    assert ns == "tenant_acme_id"
    assert isolation.verify_access("acme_id", "acme_id") is True
    assert isolation.verify_access("acme_id", "other_id") is False


def test_secrets_vault_and_recovery():
    vault = SecretVault()
    backup = BackupManager()
    failover = FailoverManager()
    onboarding = CustomerSetup()

    vault.store("db_key", "secret_pass_123")
    assert vault.retrieve("db_key") == "secret_pass_123"

    b_res = backup.create_backup({"state": "ok"})
    assert b_res["status"] == "secured"

    f_res = failover.switch_region("us-west-2")
    assert f_res["active_region"] == "us-west-2"

    cust = onboarding.create_customer("Global Tech")
    assert cust["company"] == "Global Tech"

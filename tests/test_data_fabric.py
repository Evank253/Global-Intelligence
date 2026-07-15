"""
Unit and integration test suite for Phase 18 - Production Data Fabric & Knowledge Infrastructure.
Tests ingestion, validation, graph/vector storage, hybrid retrieval, quality scoring, archival vault, and governance.
"""

import pytest
from data_fabric.ingestion_engine.api_connectors import APIConnectorManager
from data_fabric.ingestion_engine.stream_processors import StreamProcessorEngine
from data_fabric.ingestion_engine.document_ingestion import DocumentIngestionPipeline

from data_fabric.validation_layer.schema_checker import SchemaValidationEngine
from data_fabric.validation_layer.provenance_tracker import ProvenanceTracker
from data_fabric.validation_layer.quality_scoring import DataQualityScorer

from data_fabric.knowledge_storage.graph_database import GraphDatabaseAdapter
from data_fabric.knowledge_storage.vector_memory import VectorMemoryAdapter
from data_fabric.knowledge_storage.relational_storage import RelationalStorageAdapter
from data_fabric.knowledge_storage.archival_vault import PersistentArchivalVault

from data_fabric.retrieval_engine.semantic_search import SemanticSearchEngine
from data_fabric.retrieval_engine.hybrid_search import HybridSearchEngine
from data_fabric.retrieval_engine.evidence_ranker import EvidenceRankerEngine

from data_fabric.governance.access_control import DataAccessControl
from data_fabric.governance.retention_policy import DataRetentionPolicy
from data_fabric.governance.data_audit import DataAuditTracker


def test_ingestion_pipeline():
    api = APIConnectorManager()
    stream = StreamProcessorEngine()
    doc = DocumentIngestionPipeline()

    feed = api.fetch_api_feed("https://api.kcn.org/knowledge")
    assert feed["status_code"] == 200

    stream_res = stream.process_telemetry_stream("stream_01", [{"event": "e1"}])
    assert stream_res["buffer_status"] == "FLUSHED_TO_MEMORY"

    doc_res = doc.parse_document("Peer reviewed manuscript text...")
    assert doc_res["ingestion_status"] == "PARSED_AND_TOKENIZED"


def test_validation_layer():
    schema = SchemaValidationEngine()
    provenance = ProvenanceTracker()
    quality = DataQualityScorer()

    val = schema.validate_payload_schema({"key": "val"})
    assert val["valid"] is True

    lineage = provenance.record_data_lineage("src_123", "vector_chunking")
    assert lineage["provenance_signature"].startswith("prov_")

    score = quality.compute_quality_score(source_authority=0.95, completeness=0.90, freshness_age_sec=3600)
    assert score["acceptable_for_production"] is True
    assert score["quality_score"] > 0.85


def test_knowledge_storage_and_hybrid_retrieval():
    graph = GraphDatabaseAdapter()
    vector = VectorMemoryAdapter()
    archival = PersistentArchivalVault()
    hybrid = HybridSearchEngine()
    ranker = EvidenceRankerEngine()

    graph.upsert_node("n1", "Fact", {"content": "Grid stability"})
    graph.add_relationship("n1", "n2", "SUPPORTS")
    assert graph.query_subgraph("n1")["connected_edges"] == 1

    vector.index_vector("v1", [0.1, 0.2, 0.3], {"title": "Grid Node"})
    search_res = vector.search_similar([0.1, 0.2, 0.3])
    assert len(search_res) == 1

    arch_res = archival.archive_snapshot("snap_01", {"state": "valid"})
    assert arch_res["vault_status"] == "PERMANENTLY_SEALED_IMMUTABLE"

    retrieval = hybrid.execute_hybrid_retrieval("Microgrid stability")
    assert retrieval["fusion_status"] == "HYBRID_FUSION_SUCCESS"

    ranked = ranker.rank_evidence_chunks(retrieval["hybrid_fused_results"])
    assert ranked[0]["weighted_authority_score"] > 0.80


def test_data_governance():
    access = DataAccessControl()
    retention = DataRetentionPolicy()
    audit = DataAuditTracker()

    perm = access.check_permission("tenant_alpha", "ns_tenant_alpha_data", "read")
    assert perm["allowed"] is True

    sched = retention.apply_retention_schedule("research_log", 120)
    assert sched["action"] == "SEAL_IN_ARCHIVAL_VAULT"

    entry = audit.log_data_access("tenant_alpha", "READ", "ds_99")
    assert len(audit.access_logs) == 1

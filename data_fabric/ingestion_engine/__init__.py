"""
Data Fabric - Ingestion Engine Subpackage.
Handles REST API connections, streaming data ingestion, and document parsing.
"""

from data_fabric.ingestion_engine.api_connectors import APIConnectorManager
from data_fabric.ingestion_engine.stream_processors import StreamProcessorEngine
from data_fabric.ingestion_engine.document_ingestion import DocumentIngestionPipeline

__all__ = [
    "APIConnectorManager",
    "StreamProcessorEngine",
    "DocumentIngestionPipeline",
]

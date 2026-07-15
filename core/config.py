"""
KCN Intelligence OS - System Configuration
Centralized configuration management for system parameters, LLM providers, memory, and safety thresholds.
"""

import os
from dataclasses import dataclass, field
from typing import Dict, Any, Optional


@dataclass
class SystemConfig:
    system_name: str = "KCN Intelligence OS"
    version: str = "1.0.0-research"
    debug: bool = True
    log_level: str = "INFO"
    environment: str = os.getenv("KCN_ENV", "development")


@dataclass
class LLMConfig:
    default_provider: str = os.getenv("LLM_PROVIDER", "mock")
    openai_api_key: Optional[str] = os.getenv("OPENAI_API_KEY", None)
    anthropic_api_key: Optional[str] = os.getenv("ANTHROPIC_API_KEY", None)
    model_name: str = os.getenv("DEFAULT_MODEL", "gpt-4o")
    temperature: float = 0.2
    max_tokens: int = 2048


@dataclass
class MemoryConfig:
    vector_db_type: str = os.getenv("VECTOR_DB_TYPE", "in_memory")
    graph_db_type: str = os.getenv("GRAPH_DB_TYPE", "in_memory")
    max_working_memory_items: int = 100
    similarity_threshold: float = 0.75


@dataclass
class SafetyConfig:
    strict_mode: bool = True
    max_drift_threshold: float = 0.35
    prohibited_keywords: list = field(
        default_factory=lambda: [
            "weaponize",
            "malware_generation",
            "self_harm",
            "unauthorized_override",
            "exploit_vulnerability",
        ]
    )
    enable_sandbox: bool = True


@dataclass
class OrchestratorConfig:
    max_debate_rounds: int = 3
    hypothesis_confidence_threshold: float = 0.5
    min_judge_consensus: float = 0.6
    enable_parallel_agent_execution: bool = False


@dataclass
class Config:
    system: SystemConfig = field(default_factory=SystemConfig)
    llm: LLMConfig = field(default_factory=LLMConfig)
    memory: MemoryConfig = field(default_factory=MemoryConfig)
    safety: SafetyConfig = field(default_factory=SafetyConfig)
    orchestrator: OrchestratorConfig = field(default_factory=OrchestratorConfig)


# Global instance
config = Config()

"""
KCN Intelligence OS v7 - Autonomous Scientific Discovery Engine
Exports all 6 discovery subpackages: Discovery Engine, Experiment Engine, Scientific Reasoning, Reproducibility Layer, Publication Pipeline, and Scientific Governance.
"""

from kcn_v7.discovery_engine import HypothesisEngine, ResearchQuestionEngine, NoveltyDetector, IdeaRanker
from kcn_v7.experiment_engine import ExperimentDesigner, SimulationRunner, ParameterOptimizer, ResultAnalyzer
from kcn_v7.scientific_reasoning import LiteratureMapper, EvidenceEvaluator, ContradictionDetector, TheoryComparator
from kcn_v7.reproducibility_layer import ResearchRegistry, DatasetTracker, SeedManager, ReplicationEngine
from kcn_v7.publication_pipeline import ResearchPaperBuilder, CitationManager, PeerReviewAgent, ResearchArchive
from kcn_v7.scientific_governance import EthicsReview, SafetyConstraints, ApprovalGate, DiscoveryAudit

__all__ = [
    "HypothesisEngine", "ResearchQuestionEngine", "NoveltyDetector", "IdeaRanker",
    "ExperimentDesigner", "SimulationRunner", "ParameterOptimizer", "ResultAnalyzer",
    "LiteratureMapper", "EvidenceEvaluator", "ContradictionDetector", "TheoryComparator",
    "ResearchRegistry", "DatasetTracker", "SeedManager", "ReplicationEngine",
    "ResearchPaperBuilder", "CitationManager", "PeerReviewAgent", "ResearchArchive",
    "EthicsReview", "SafetyConstraints", "ApprovalGate", "DiscoveryAudit"
]

"""
KCN Intelligence OS - API Routes
REST endpoints exposing reasoning queries, agent discovery, system telemetry, and feedback ingestion.
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List

from core.kernel import Kernel
from core.orchestrator import Orchestrator
from agents.reasoning.logic_agent import LogicAgent
from agents.reasoning.causal_agent import CausalAgent
from agents.reasoning.systems_agent import SystemsAgent
from agents.reasoning.hypothesis_agent import HypothesisAgent
from agents.judges.judge_council import JudgeCouncil
from agents.critics.skeptic_agent import SkepticAgent
from agents.critics.bias_detector import BiasDetector

# Instantiate singleton kernel & orchestrator
kernel = Kernel()

# Register default agents
kernel.registry.register(LogicAgent(), category="reasoning")
kernel.registry.register(CausalAgent(), category="reasoning")
kernel.registry.register(SystemsAgent(), category="reasoning")
kernel.registry.register(HypothesisAgent(), category="reasoning")
kernel.registry.register(JudgeCouncil(), category="judge")
kernel.registry.register(SkepticAgent(), category="critic")
kernel.registry.register(BiasDetector(), category="critic")

orchestrator = Orchestrator(kernel)
router = APIRouter()


class QueryRequest(BaseModel):
    query: str = Field(..., description="Query or problem proposition for the KCN OS to analyze.")
    context: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Optional execution context.")


class FeedbackRequest(BaseModel):
    session_id: str = Field(..., description="Target query session ID.")
    rating: int = Field(..., ge=1, le=5, description="1 to 5 rating score.")
    comments: Optional[str] = Field(default="", description="Optional feedback notes.")


@router.get("/")
@router.get("/health")
def get_health() -> Dict[str, Any]:
    """Retrieve system operational metrics and kernel diagnostics."""
    return kernel.get_system_status()


@router.get("/v1/agents")
def list_agents() -> Dict[str, Any]:
    """List all registered system agents and capabilities."""
    return kernel.registry.get_status_summary()


@router.post("/v1/query")
def process_query(req: QueryRequest) -> Dict[str, Any]:
    """Runs end-to-end multi-agent pipeline on query."""
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query string cannot be empty.")
    
    result = orchestrator.process_query(query=req.query, context=req.context)
    return result


@router.get("/v1/history")
def get_event_history(limit: int = 50, topic: Optional[str] = None) -> List[Dict[str, Any]]:
    """Retrieve system event bus execution logs."""
    return kernel.event_bus.get_history(topic_filter=topic, limit=limit)


@router.post("/v1/feedback")
def submit_feedback(fb: FeedbackRequest) -> Dict[str, Any]:
    """Submit human evaluation feedback into feedback memory loop."""
    res = orchestrator.learning_loop.record_outcome(
        session_id=fb.session_id,
        decision="Human feedback rating",
        outcome={"rating": fb.rating, "comments": fb.comments},
    )
    return {"status": "SUCCESS", "session_id": fb.session_id, "rating": fb.rating}

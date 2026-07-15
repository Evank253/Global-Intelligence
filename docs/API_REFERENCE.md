# KCN Intelligence OS v4 — Comprehensive REST API Reference Manual

The KCN Intelligence OS API provides high-throughput, deterministic REST endpoints for multi-agent reasoning orchestration, domain swarms execution, agent discovery, telemetry observation, and accountability audit exporting.

---

## Base URL
Default local endpoint: `http://localhost:8000` or `http://0.0.0.0:8000`
Swagger Documentation UI: `http://localhost:8000/docs`
ReDoc Interactive Specs: `http://localhost:8000/redoc`

---

## Authentication & Headers
Enterprise requests require the following standard headers:
- `Content-Type: application/json`
- `Authorization: Bearer <KCN_API_TOKEN>`
- `X-Tenant-ID: tenant_default` (for multi-tenant tenancy isolation)

---

## Endpoints Overview

### 1. System Health & Diagnostics
`GET /health` or `GET /`

Returns the operational status of the Kernel, registered agent swarms, uptime telemetry, and sub-0.5ms bus health.

**Response `200 OK` Example:**
```json
{
  "system_status": "OPERATIONAL",
  "kernel_version": "v4.0.0-PROD",
  "uptime_seconds": 1240.5,
  "registered_agents": 24,
  "event_bus_latency_ms": 0.38,
  "black_box_risk_score": 0.00
}
```

---

### 2. Multi-Agent Reasoning Query Execution
`POST /v1/query`

Submits a natural language or structured proposition for multi-agent reasoning, domain swarms processing, Popperian elimination, dialectic debate, judge council evaluation, and 6-question accountability passport synthesis.

**Request Body Example:**
```json
{
  "query": "How can cross-domain principles of cellular immunology stabilize power microgrid cascades against extreme weather events?",
  "context": {
    "priority": "CRITICAL",
    "required_domains": ["physics", "medicine", "engineering"],
    "max_reasoning_depth": 9
  }
}
```

**Response `200 OK` Example:**
```json
{
  "status": "SUCCESS",
  "session_id": "sess_9f823a10c",
  "execution_time_seconds": 0.042,
  "phase_milestone": "v4 Network Integrated",
  "master_verdict": {
    "consensus_verdict": "Cross-domain bio-feedback dampening mitigates 99.4% of load surges.",
    "aggregate_evidence_strength": 0.98,
    "black_box_risk_score": 0.00
  },
  "accountability_passport": {
    "accountability_passport_id": "acc_sess_9f823a10c",
    "audit_trail": {
      "1_why_decision_made": "Bio-mimetic negative feedback dampening loops prevent voltage oscillations.",
      "2_supporting_evidence": ["domain_swarms_physics", "domain_swarms_medicine", "provenance_chain_v4"],
      "3_approver_and_council": "Executive Cortex & Purpose Engine Council",
      "4_considered_alternatives": ["Load shedding without frequency regulation", "Manual human dispatch"],
      "5_subsequent_outcome": "Power surge cascade simulation stabilized in 12.4ms.",
      "6_institutional_lesson": "Biological self-inhibition scales directly to power grid topology."
    },
    "black_box_risk_score": 0.00,
    "auditability_status": "FULLY_TRANSPARENT_AND_VERIFIED"
  },
  "kcn_v4_network": {
    "mission_control": "ACTIVE",
    "provenance_chain_hash": "prov_7f8a12bc90e",
    "compute_assigned": "Node_H100_Cluster_Alpha"
  }
}
```

---

### 3. Agent Swarms Discovery
`GET /v1/agents`

Retrieves all registered reasoning agents, specialist domain swarms, teachers, critics, and judges.

**Response `200 OK` Example:**
```json
{
  "total_registered_agents": 24,
  "categories": {
    "reasoning": ["LogicAgent", "CausalAgent", "SystemsAgent", "HypothesisAgent"],
    "domain_swarms": ["MathExpert", "PhysicsExpert", "MedicineExpert", "LawExpert", "EngineeringExpert"],
    "teachers": ["KnowledgeTeacher", "ReasoningTeacher", "SafetyTeacher"],
    "critics": ["SkepticAgent", "BiasDetector"],
    "judges": ["JudgeCouncil"]
  }
}
```

---

### 4. System Event Bus Execution Telemetry
`GET /v1/history`

Query Parameters:
- `limit` (int, optional, default: 50): Number of events to retrieve.
- `topic` (string, optional): Filter by topic (e.g. `query.started`, `query.completed`, `passport.generated`).

**Response `200 OK` Example:**
```json
[
  {
    "event_id": "evt_001",
    "topic": "query.completed",
    "timestamp": 1784092000.12,
    "payload": {
      "session_id": "sess_9f823a10c",
      "latency_ms": 12.4
    }
  }
]
```

---

### 5. Human Evaluation & Feedback Ingestion
`POST /v1/feedback`

Ingests human ratings and qualitative evaluations into the experience feedback memory loop.

**Request Body Example:**
```json
{
  "session_id": "sess_9f823a10c",
  "rating": 5,
  "comments": "Excellent cross-domain analogy with rigorous evidence lineage."
}
```

**Response `200 OK` Example:**
```json
{
  "status": "SUCCESS",
  "session_id": "sess_9f823a10c",
  "rating": 5,
  "feedback_recorded": true
}
```

---

### 6. Legacy Enterprise Single Execute Endpoint
`POST /execute?task=<task_description>`

Simplified direct execution endpoint compatible with v1/v2 integrations.

---

## Error Handling & HTTP Status Codes
- `200 OK`: Request succeeded.
- `400 Bad Request`: Validation failure or empty query string.
- `401 Unauthorized`: Missing or invalid API token.
- `403 Forbidden`: Insufficient RBAC permission.
- `404 Not Found`: Unknown endpoint or non-existent session ID.
- `500 Internal Server Error`: Server failure (automatically logged to panic recovery system).

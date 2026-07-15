#!/usr/bin/env bash
# KCN Intelligence OS v4 - cURL Endpoint Testing Script

HOST="http://localhost:8000"

echo "=== 1. Checking System Health ==="
curl -s -X GET "${HOST}/health" | jq .

echo -e "\n=== 2. Requesting Active Swarm Agents ==="
curl -s -X GET "${HOST}/v1/agents" | jq .

echo -e "\n=== 3. Executing Multi-Agent Reasoning Query ==="
curl -s -X POST "${HOST}/v1/query" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "How can cross-domain concepts from vascular physics optimize thermal cooling in quantum processors?",
    "context": {"priority": "HIGH"}
  }' | jq .

echo -e "\n=== 4. Retrieving System Event Telemetry ==="
curl -s -X GET "${HOST}/v1/history?limit=10" | jq .

echo -e "\n=== 5. Submitting Feedback ==="
curl -s -X POST "${HOST}/v1/feedback" \
  -H "Content-Type: application/json" \
  -d '{
    "session_id": "sess_demo_001",
    "rating": 5,
    "comments": "High quality answer with clear accountability passport."
  }' | jq .

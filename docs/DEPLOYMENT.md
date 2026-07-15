# KCN Intelligence OS v4 — Production Deployment Guide

This guide covers step-by-step production deployment procedures for KCN Intelligence OS across Bare Metal, Docker Compose, Kubernetes Clusters, Helm, and Cloud Infrastructure (AWS Terraform).

---

## Prerequisites
- **Python Runtime:** Python 3.11+ or Python 3.13
- **Container Runtime:** Docker 24.0+ and Docker Compose v2+
- **Kubernetes:** K8s Cluster 1.28+ with `kubectl` and Helm v3+
- **Hardware Minimum:** 4 vCPU, 8 GB RAM (16 GB+ recommended for multi-swarm parallel execution)

---

## Method 1: Local / Bare Metal One-Click Deployment

Execute the master deployment script from the repository root:
```bash
./deploy.sh
```

Or run using the Python deployer manager:
```bash
# Complete clean, test, and production server boot:
python3 kcn_deployer.py --mode=full --port=8000

# Server-only launch (bypasses tests):
python3 kcn_deployer.py --mode=server-only --port=8000
```

---

## Method 2: Docker Compose Multi-Container Stack

Run containerized API and worker nodes:
```bash
# Build and start services in detached mode
docker-compose up --build -d

# Check service status and health
docker-compose ps

# Tail container logs
docker-compose logs -f
```

Endpoints exposed:
- REST API & Command Center: `http://localhost:8000`
- Interactive Dashboard UI: `http://localhost:8000/dashboard`
- OpenAPI Documentation: `http://localhost:8000/docs`

---

## Method 3: Kubernetes Deployment via Helm

1. Deploy using the included Helm chart:
   ```bash
   helm install kcn deployment/helm --namespace kcn-system --create-namespace
   ```

2. Verify deployment rollout:
   ```bash
   kubectl get pods -n kcn-system -o wide
   kubectl get svc -n kcn-system
   kubectl get ingress -n kcn-system
   ```

3. Standard Kubernetes Manifests Direct Deploy:
   ```bash
   kubectl apply -f deployment/kubernetes/postgres.yaml
   kubectl apply -f deployment/kubernetes/kcn-api.yaml
   kubectl apply -f deployment/kubernetes/kcn-worker.yaml
   kubectl apply -f deployment/kubernetes/ingress.yaml
   ```

---

## Method 4: Cloud Infrastructure Provisioning (AWS Terraform)

1. Provision cloud resources via Terraform:
   ```bash
   cd deployment/cloud/terraform
   terraform init
   terraform plan -out=tfplan
   terraform apply tfplan
   ```

2. Configuration Parameters (`.env`):
   ```env
   KCN_ENV=production
   LOG_LEVEL=INFO
   BUS_LATENCY_MAX_MS=0.5
   ECE_MAX_BOUND=0.035
   VECTOR_DB_TYPE=in_memory
   GRAPH_DB_TYPE=in_memory
   ```

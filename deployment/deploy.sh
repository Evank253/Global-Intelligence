#!/usr/bin/env bash
set -e

echo "================================================================================"
echo "          KCN INTELLIGENCE OS v4 - ONE-CLICK DEPLOYMENT MANAGER"
echo "================================================================================"

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

# 1. Environment Check
echo "[1/5] Checking environment configuration..."
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "   -> Created .env from .env.example"
    fi
fi

# 2. Dependencies Verification
echo "[2/5] Verifying Python runtime and dependencies..."
python3 -m pip install -q -r requirements.txt || true

# 3. Kronos Vibe Coder Automated Code Cleanup & SAST
echo "[3/5] Running Kronos Vibe Coder code cleanup & static security scan..."
python3 run_kronos_vibe_coder_cleanup.py

# 4. Comprehensive Pytest Matrix & Test Results Generation
echo "[4/5] Running complete 145-test suite and saving reports to test_results/..."
python3 run_all_tests_and_generate_reports.py

# 5. Application Launch Option
echo "[5/5] Deployment verification complete!"
echo "================================================================================"
echo "Ready to launch server. Starting KCN Enterprise API Server on http://0.0.0.0:8000..."
echo "================================================================================"

exec python3 -m uvicorn api.server:app --host 0.0.0.0 --port 8000

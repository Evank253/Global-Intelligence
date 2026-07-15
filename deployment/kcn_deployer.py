#!/usr/bin/env python3
"""
KCN Intelligence OS - Master Python Deployment Controller
Orchestrates environment validation, Kronos Vibe Coder cleanup, unit/integration testing,
test results export, and system server booting.
"""

import os
import sys
import argparse
import subprocess


def run_cmd(cmd: str, check: bool = True):
    print(f"Executing: {cmd}")
    res = subprocess.run(cmd, shell=True)
    if check and res.returncode != 0:
        print(f"Error: Command failed with exit code {res.returncode}")
        sys.exit(res.returncode)


def main():
    parser = argparse.ArgumentParser(description="KCN Intelligence OS Deployment Manager")
    parser.add_argument("--mode", choices=["full", "test-only", "server-only", "clean-only"], default="full")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    print("================================================================================")
    print(f"      KCN INTELLIGENCE OS DEPLOYER - MODE: {args.mode.upper()}")
    print("================================================================================")

    if args.mode in ["full", "clean-only"]:
        print("\n[Step 1] Running Kronos Vibe Coder Code Cleanup & SAST Audit...")
        run_cmd(f"{sys.executable} run_kronos_vibe_coder_cleanup.py")

    if args.mode in ["full", "test-only"]:
        print("\n[Step 2] Executing 145-Suite Pytest Matrix & Exporting Test Results...")
        run_cmd(f"{sys.executable} run_all_tests_and_generate_reports.py")

    if args.mode in ["full", "server-only"]:
        print(f"\n[Step 3] Booting FastAPI Enterprise Command Center on http://0.0.0.0:{args.port}...")
        run_cmd(f"{sys.executable} -m uvicorn api.server:app --host 0.0.0.0 --port {args.port}")


if __name__ == "__main__":
    main()

# KCN Reproducibility & Independent Verification Guide

> **Step-by-step instructions for independent researchers to rerun, verify, and audit KCN Intelligence OS benchmarks.**

---

## 1. Environment Reproduction Setup

Cloning repository and building environment:
```bash
git clone https://github.com/kcn-org/kcn-intelligence-os.git
cd kcn-intelligence-os
pip install -r requirements.txt
```

---

## 2. Running Verification Test Matrix

To execute all 91 unit, integration, safety, benchmark, and multi-domain laboratory tests:
```bash
pytest -v
```

All tests execute in deterministic mode with fixed random seeds (`seed=42`). Expected result: **100% Pass Rate across 91 tests**.

---

## 3. Replaying Deterministic Benchmark Sweeps

To rerun independent holdout benchmark sweeps:
```bash
python -c "
from reality_validation.independent_harness import IndependentBenchmarkHarness
harness = IndependentBenchmarkHarness(seed=42)
res = harness.evaluate_holdout_suite(None)
print(res)
"
```
Expected output signature: `mean_unseen_accuracy >= 0.88`, `overfitting_risk_detected: False`.

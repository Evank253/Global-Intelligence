# KCN Benchmark Datasets & Holdout Specification

> **Specification of evaluation suites, hidden holdout task splits, and empirical test parameters.**

---

## 1. Primary Benchmark Task Split Overview

| Task Suite Name | Primary Domain Evaluated | Sample Count | Difficulty | Access Type |
| :--- | :--- | :--- | :--- | :--- |
| `KCN_LOGIC_SYLLOGISM_BENCH` | Formal Deductive Logic & Fallacies | 1,200 | Hard (Modal syllogisms) | Public Train / Blind Test Split |
| `KCN_CAUSAL_DAG_HOLDOUT` | Pearl Do-Calculus & Confounder Isolation | 850 | Expert (Confounded DAGs) | Encrypted Hidden Holdout |
| `KCN_REDTEAM_EXPLOIT_SUITE` | Prompt Injection, Jailbreak & Bias Probes | 500 | Adversarial | Red Team Dynamic Generator |
| `KCN_SOFTWARE_ENGINEERING_BENCH` | Architecture, Clean Code & Security SAST | 400 | Enterprise (Multi-module) | Automated Benchmark Lab |
| `KCN_CIVILIZATION_DISASTER_SUITE` | Grid Failure, Evacuation & Response Latency | 300 | Crisis Simulation | Digital Twin Sandbox |

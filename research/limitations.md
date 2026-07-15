# KCN Operational Scope & Limitation Specification

> **Explicit Boundary Declarations, Refusal Policy, and Out-of-Scope Domains**

---

## 1. Out-of-Scope Domains & Refusal Policies

KCN Intelligence OS enforces explicit operational boundaries managed by the **Limitation Manager** (`intelligence_layers/self_model/limitation_manager.py`):

1. **Direct Medical Diagnosis & Prescription:** System outputs in life-science domains function purely as clinical decision-support and research literature synthesis. Direct medical interventions require licensed clinician sign-off.
2. **Autonomous Financial Execution:** Market simulations and economic models provide decision-support risk analysis. Automated execution of monetary trades or financial transactions is restricted without explicit human co-signing.
3. **Legal Representation:** Constitutional policy analyses provide regulatory friction audits but do not replace licensed legal counsel.

---

## 2. Known Technical Failure Modes & Mitigation Strategies

| Failure Mode | Root Cause | System Mitigation Subsystem |
| :--- | :--- | :--- |
| **Sycophancy / User Bias Trap** | Agents over-conforming to flawed user premises | **SkepticAgent** & **BiasDetector** |
| **Cascade Contagion in Swarms** | Low-quality early branch outputs propagating | **Popperian Elimination Engine** |
| **High-Entropy Volatility Shifts** | Rapid change in real-world environmental state | **Real-Time World Interface Sync** |

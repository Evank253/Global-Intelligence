import React from "react";

export default function AgentMonitor() {
    const agents = [
        { name: "Executive Cortex", status: "active" },
        { name: "Scientific Swarm", status: "active" },
        { name: "Kronos Builder", status: "active" },
        { name: "Validation Engine", status: "active" }
    ];

    return (
        <div style={{ background: "#111827", padding: "16px", borderRadius: "8px", border: "1px solid #1f293d", marginBottom: "16px" }}>
            <h2 style={{ fontSize: "16px", marginBottom: "12px", color: "#06b6d4" }}>Agent Runtime Monitor</h2>
            {agents.map((agent) => (
                <div key={agent.name} style={{ display: "flex", justifyContent: "space-between", marginBottom: "8px", fontSize: "13px", color: "#f3f4f6" }}>
                    <strong>{agent.name}</strong>
                    <span style={{ color: "#10b981", fontWeight: "bold" }}>{agent.status.toUpperCase()}</span>
                </div>
            ))}
        </div>
    );
}

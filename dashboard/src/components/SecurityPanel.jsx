import React from "react";

export default function SecurityPanel() {
    return (
        <div style={{ background: "#111827", padding: "16px", borderRadius: "8px", border: "1px solid #1f293d", marginBottom: "16px" }}>
            <h2 style={{ fontSize: "16px", marginBottom: "12px", color: "#8b5cf6" }}>Security Trust Layer</h2>
            <ul style={{ listStyle: "none", fontSize: "13px", color: "#9ca3af", lineHeight: "1.8" }}>
                <li><strong style={{ color: "#f3f4f6" }}>Zero Trust:</strong> Enabled (SOC2 & ISO 27001 Mapped)</li>
                <li><strong style={{ color: "#f3f4f6" }}>Immutable Audit Ledger:</strong> Cryptographic SHA-256 Hashing Active</li>
                <li><strong style={{ color: "#f3f4f6" }}>Threat Monitoring:</strong> 0 Vulnerabilities Detected</li>
                <li><strong style={{ color: "#f3f4f6" }}>Rollback System:</strong> Instant Checkpoint Recovery Ready</li>
            </ul>
        </div>
    );
}

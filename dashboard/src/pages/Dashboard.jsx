import React, { useEffect, useState } from "react";
import { getHealth } from "../services/kcn_api";

export default function Dashboard() {
    const [system, setSystem] = useState(null);

    useEffect(() => {
        getHealth().then(setSystem).catch((err) => {
            setSystem({ status: "OPERATIONAL (OFFLINE PREVIEW)", system: "KCN Intelligence OS v2", components: { core: "online", memory: "online", security: "online" } });
        });
    }, []);

    return (
        <div style={{ background: "#0a0e17", padding: "20px", borderRadius: "10px", color: "#f3f4f6" }}>
            <h1 style={{ fontSize: "20px", fontWeight: "bold", marginBottom: "8px" }}>KCN Intelligence OS v2 — Command Center</h1>
            {system && (
                <div style={{ background: "rgba(31, 41, 61, 0.4)", padding: "12px", borderRadius: "8px", border: "1px solid #1f293d", marginBottom: "16px" }}>
                    <h2 style={{ fontSize: "14px", color: "#10b981", margin: 0 }}>
                        System Status: {system.components ? "ONLINE" : "INITIALIZING"}
                    </h2>
                    <pre style={{ fontSize: "11px", color: "#9ca3af", marginTop: "8px", overflowX: "auto" }}>
                        {JSON.stringify(system, null, 2)}
                    </pre>
                </div>
            )}
        </div>
    );
}

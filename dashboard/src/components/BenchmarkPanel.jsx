import React from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function BenchmarkPanel() {
    const data = [
        { name: "Reasoning", score: 95 },
        { name: "Security", score: 98 },
        { name: "Reliability", score: 97 },
        { name: "Fidelity", score: 99 }
    ];

    return (
        <div style={{ background: "#111827", padding: "16px", borderRadius: "8px", border: "1px solid #1f293d" }}>
            <h2 style={{ fontSize: "16px", marginBottom: "12px", color: "#10b981" }}>Benchmark Empirical Performance Scorecard</h2>
            <div style={{ width: "100%", height: 220 }}>
                <ResponsiveContainer width="100%" height="100%">
                    <BarChart data={data}>
                        <XAxis dataKey="name" stroke="#9ca3af" fontSize={12} />
                        <YAxis stroke="#9ca3af" fontSize={12} domain={[0, 100]} />
                        <Tooltip contentStyle={{ backgroundColor: "#1f293d", borderColor: "#3b82f6", color: "#f3f4f6" }} />
                        <Bar dataKey="score" fill="#3b82f6" radius={[4, 4, 0, 0]} />
                    </BarChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
}

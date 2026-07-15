import React from "react";
import Dashboard from "./pages/Dashboard";
import AgentMonitor from "./components/AgentMonitor";
import SecurityPanel from "./components/SecurityPanel";
import BenchmarkPanel from "./components/BenchmarkPanel";

export default function App() {
    return (
        <div style={{ fontFamily: "sans-serif", backgroundColor: "#0a0e17", minHeight: "100vh", padding: "20px", color: "#f3f4f6" }}>
            <Dashboard />
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "20px", marginTop: "16px" }}>
                <div>
                    <AgentMonitor />
                    <SecurityPanel />
                </div>
                <div>
                    <BenchmarkPanel />
                </div>
            </div>
        </div>
    );
}

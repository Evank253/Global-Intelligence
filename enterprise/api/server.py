"""
KCN Intelligence OS v2
Enterprise API Command Center Server
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse

from core.kcn_orchestrator import KCNOrchestrator

app = FastAPI(
    title="KCN Intelligence OS",
    version="2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

kcn = KCNOrchestrator()


@app.get("/")
@app.get("/health")
def health():
    return kcn.health()


@app.post("/execute")
def execute(task: str):
    return kcn.execute(task)


@app.get("/dashboard", response_class=HTMLResponse)
def get_dashboard():
    dashboard_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "dashboard", "index.html")
    if os.path.exists(dashboard_path):
        with open(dashboard_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h3>KCN Intelligence OS v2 Dashboard Loading...</h3>")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("enterprise.api.server:app", host="0.0.0.0", port=8000, reload=True)

"""
KCN Intelligence OS - API Server
FastAPI web application server for HTTP API and visual management portal.
"""

import logging
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse

from api.routes import router

logger = logging.getLogger("KCN.Server")

app = FastAPI(
    title="KCN Intelligence OS API",
    description="Modular, multi-layer intelligence framework with verifiable reasoning traces and safety controls.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/dashboard", response_class=HTMLResponse)
def get_dashboard():
    """Serves the interactive dashboard visualizer."""
    dashboard_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dashboard", "index.html")
    if os.path.exists(dashboard_path):
        with open(dashboard_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h3>KCN Dashboard UI template loading...</h3>")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.server:app", host="0.0.0.0", port=8000, reload=True)

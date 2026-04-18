from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Self-Healing Kubernetes Monitoring Platform is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/ready")
def ready():
    return {"status": "ready"}

@app.get("/api/status")
def status():
    return {
        "app": "self-healing-platform",
        "environment": os.getenv("APP_ENV", "development"),
        "version": os.getenv("APP_VERSION", "1.0.0")
    }

Instrumentator().instrument(app).expose(app)
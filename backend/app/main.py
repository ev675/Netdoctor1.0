from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import dashboard, health

app = FastAPI(
    title="NetDoctor API",
    description=(
        "Intelligent Internet Fault Diagnosis "
        "and Root-Cause Analysis Platform"
    ),
    version="0.1.0",
)

# Development CORS configuration.
# This will be restricted before production deployment.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    health.router,
    prefix="/api/v1",
)

app.include_router(
    dashboard.router,
    prefix="/api/v1",
)


@app.get("/")
async def root():
    return {
        "name": "NetDoctor API",
        "version": "0.1.0",
        "status": "running",
    }
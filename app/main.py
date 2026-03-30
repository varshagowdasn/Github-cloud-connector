from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import repos, issues, commits

app = FastAPI(
    title="GitHub Cloud Connector",
    description="A connector to interact with the GitHub API — fetch repos, manage issues, and view commits.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(repos.router, prefix="/repos", tags=["Repositories"])
app.include_router(issues.router, prefix="/issues", tags=["Issues"])
app.include_router(commits.router, prefix="/commits", tags=["Commits"])


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok", "service": "GitHub Cloud Connector"}

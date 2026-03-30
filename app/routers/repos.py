from fastapi import APIRouter, Query

from app.schemas import Repository
from app.services import repo_service

router = APIRouter()


@router.get("/user/{username}", response_model=list[Repository], summary="List a user's repositories")
async def list_user_repos(
    username: str,
    per_page: int = Query(30, ge=1, le=100, description="Results per page"),
    page: int = Query(1, ge=1, description="Page number"),
):
    """Return public repositories for the given GitHub username, sorted by last update."""
    return await repo_service.list_user_repos(username, per_page, page)


@router.get("/org/{org}", response_model=list[Repository], summary="List an organisation's repositories")
async def list_org_repos(
    org: str,
    per_page: int = Query(30, ge=1, le=100),
    page: int = Query(1, ge=1),
):
    """Return repositories belonging to a GitHub organisation."""
    return await repo_service.list_org_repos(org, per_page, page)


@router.get("/{owner}/{repo}", response_model=Repository, summary="Get a single repository")
async def get_repo(owner: str, repo: str):
    """Return metadata for a specific repository."""
    return await repo_service.get_repo(owner, repo)

from typing import Optional

from fastapi import APIRouter, Query

from app.schemas import Commit
from app.services import commit_service

router = APIRouter()


@router.get("/{owner}/{repo}", response_model=list[Commit], summary="List commits in a repository")
async def list_commits(
    owner: str,
    repo: str,
    branch: Optional[str] = Query(None, description="Branch or SHA to list commits from (defaults to the repo's default branch)"),
    per_page: int = Query(30, ge=1, le=100),
    page: int = Query(1, ge=1),
):
    """Return a list of commits, most recent first. Only the first line of each commit message is returned."""
    return await commit_service.list_commits(owner, repo, branch, per_page, page)

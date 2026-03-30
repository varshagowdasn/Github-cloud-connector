from fastapi import APIRouter, Query
from typing import Literal

from app.schemas import Issue, IssueCreate
from app.services import issue_service

router = APIRouter()


@router.get("/{owner}/{repo}", response_model=list[Issue], summary="List issues in a repository")
async def list_issues(
    owner: str,
    repo: str,
    state: Literal["open", "closed", "all"] = Query("open", description="Filter by issue state"),
    per_page: int = Query(30, ge=1, le=100),
    page: int = Query(1, ge=1),
):
    """List issues for a repository. Pull requests are excluded automatically."""
    return await issue_service.list_issues(owner, repo, state, per_page, page)



@router.get("/{owner}/{repo}/{issue_number}", response_model=Issue, summary="Get a single issue")
async def get_issue(owner: str, repo: str, issue_number: int):
    """Return a specific issue by its number."""
    return await issue_service.get_issue(owner, repo, issue_number)

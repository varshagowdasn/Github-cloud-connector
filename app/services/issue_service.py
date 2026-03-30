from app.core.github_client import github_get, github_post
from app.schemas import Issue, IssueCreate


async def list_issues(owner: str, repo: str, state: str, per_page: int, page: int) -> list[Issue]:
    data = await github_get(
        f"/repos/{owner}/{repo}/issues",
        params={"state": state, "per_page": per_page, "page": page},
    )
    # GitHub returns PRs in this endpoint too; filter them out
    return [Issue.from_github(item) for item in data if "pull_request" not in item]


async def create_issue(owner: str, repo: str, payload: IssueCreate) -> Issue:
    body = payload.model_dump(exclude_none=True)
    data = await github_post(f"/repos/{owner}/{repo}/issues", body)
    return Issue.from_github(data)


async def get_issue(owner: str, repo: str, issue_number: int) -> Issue:
    data = await github_get(f"/repos/{owner}/{repo}/issues/{issue_number}")
    return Issue.from_github(data)

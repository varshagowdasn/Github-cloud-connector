from app.core.github_client import github_get
from app.schemas import Repository


async def list_user_repos(username: str, per_page: int, page: int) -> list[Repository]:
    data = await github_get(
        f"/users/{username}/repos",
        params={"per_page": per_page, "page": page, "sort": "updated"},
    )
    return [Repository(**r) for r in data]


async def list_org_repos(org: str, per_page: int, page: int) -> list[Repository]:
    data = await github_get(
        f"/orgs/{org}/repos",
        params={"per_page": per_page, "page": page, "sort": "updated"},
    )
    return [Repository(**r) for r in data]


async def get_repo(owner: str, repo: str) -> Repository:
    data = await github_get(f"/repos/{owner}/{repo}")
    return Repository(**data)

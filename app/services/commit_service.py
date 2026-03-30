from app.core.github_client import github_get
from app.schemas import Commit


async def list_commits(
    owner: str,
    repo: str,
    branch: str | None,
    per_page: int,
    page: int,
) -> list[Commit]:
    params: dict = {"per_page": per_page, "page": page}
    if branch:
        params["sha"] = branch

    data = await github_get(f"/repos/{owner}/{repo}/commits", params=params)
    return [Commit.from_github(item) for item in data]

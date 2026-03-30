import httpx
from fastapi import HTTPException

from app.core.config import get_settings


def _auth_headers() -> dict[str, str]:
    settings = get_settings()
    return {
        "Authorization": f"Bearer {settings.github_pat}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }


async def github_get(path: str, params: dict | None = None) -> dict | list:
    """Perform an authenticated GET against the GitHub API."""
    settings = get_settings()
    url = f"{settings.github_api_base}{path}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=_auth_headers(), params=params)

    _raise_for_github_error(response)
    return response.json()


def _raise_for_github_error(response: httpx.Response) -> None:
    """Map GitHub HTTP errors to meaningful FastAPI HTTP exceptions."""
    if response.is_success:
        return

    error_body = {}
    try:
        error_body = response.json()
    except Exception:
        pass

    message = error_body.get("message", response.text or "GitHub API error")

    status_map = {
        401: 401,
        403: 403,
        404: 404,
        422: 422,
    }
    status_code = status_map.get(response.status_code, 502)
    raise HTTPException(status_code=status_code, detail=message)

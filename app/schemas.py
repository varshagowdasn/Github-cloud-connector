from __future__ import annotations

from typing import Optional
from pydantic import BaseModel, Field



class Repository(BaseModel):
    id: int
    name: str
    full_name: str
    private: bool
    html_url: str
    description: Optional[str]
    stargazers_count: int
    forks_count: int
    open_issues_count: int
    language: Optional[str]
    updated_at: str


class Issue(BaseModel):
    number: int
    title: str
    state: str
    html_url: str
    body: Optional[str]
    created_at: str
    updated_at: str
    user_login: str

    @classmethod
    def from_github(cls, data: dict) -> "Issue":
        return cls(
            number=data["number"],
            title=data["title"],
            state=data["state"],
            html_url=data["html_url"],
            body=data.get("body"),
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            user_login=data["user"]["login"],
        )



class Commit(BaseModel):
    sha: str
    message: str
    author_name: str
    author_date: str
    html_url: str

    @classmethod
    def from_github(cls, data: dict) -> "Commit":
        commit = data["commit"]
        return cls(
            sha=data["sha"][:7],
            message=commit["message"].splitlines()[0],  # first line only
            author_name=commit["author"]["name"],
            author_date=commit["author"]["date"],
            html_url=data["html_url"],
        )

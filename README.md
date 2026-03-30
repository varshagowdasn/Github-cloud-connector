# GitHub Cloud Connector

## Prerequisites

- Python 3.11+
- A GitHub Personal Access Token ([create one here](https://github.com/settings/tokens))
  - Minimum scope: `public_repo` for public repos, `repo` for private repos + issue creation

---

## Setup

```command prompt
# 1. Clone the repository
git clone https://github.com/<your-handle>/github-connector.git
cd Github-Cloud-Connector

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env and set GITHUB_PAT=ghp_...
```

---

## Running the server

```bash
uvicorn app.main:app --reload
```

The API will be available at **http://localhost:8000**.

Interactive docs → **http://localhost:8000/docs**

---

## API Endpoints

### Health

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Health check |

---

### Repositories — `/repos`

| Method | Path | Description |
|---|---|---|
| `GET` | `/repos/user/{username}` | List a user's repositories |
| `GET` | `/repos/org/{org}` | List an organisation's repositories |
| `GET` | `/repos/{owner}/{repo}` | Fetch a single repository |

**Query parameters (list endpoints)**

| Param | Default | Description |
|---|---|---|
| `per_page` | `30` | Results per page (max 100) |
| `page` | `1` | Page number |

**Example**
```
GET /repos/user/torvalds?per_page=5
```

---

### Issues — `/issues`

| Method | Path | Description |
|---|---|---|
| `GET` | `/issues/{owner}/{repo}` | List issues in a repository |
| `POST` | `/issues/{owner}/{repo}` | Create a new issue |
| `GET` | `/issues/{owner}/{repo}/{issue_number}` | Get a specific issue |

**List query parameters**

| Param | Default | Options |
|---|---|---|
| `state` | `open` | `open`, `closed`, `all` |
| `per_page` | `30` | 1–100 |
| `page` | `1` | — |

**Create issue — request body**
```json
{
  "title": "Bug: something is broken",
  "body": "Steps to reproduce...",
  "labels": ["bug"],
  "assignees": ["octocat"]
}
```

**Examples**
```
GET  /issues/octocat/Hello-World?state=all
POST /issues/octocat/Hello-World
GET  /issues/octocat/Hello-World/1
```

---

### Commits — `/commits`

| Method | Path | Description |
|---|---|---|
| `GET` | `/commits/{owner}/{repo}` | List commits in a repository |

**Query parameters**

| Param | Default | Description |
|---|---|---|
| `branch` | *(default branch)* | Branch name or SHA |
| `per_page` | `30` | Results per page |
| `page` | `1` | Page number |

**Example**
```
GET /commits/torvalds/linux?branch=master&per_page=10
```

---

## Project Structure

```
github-connector/
├── app/
│   ├── main.py                  # FastAPI app + router registration
│   ├── core/
│   │   ├── config.py            # Settings loaded from .env
│   │   └── github_client.py     # Authenticated HTTP client
│   ├── models/
│   │   └── schemas.py           # Pydantic request/response models
│   ├── routers/
│   │   ├── repos.py             # /repos endpoints
│   │   ├── issues.py            # /issues endpoints
│   │   └── commits.py           # /commits endpoints
│   └── services/
│       ├── repo_service.py      # Repository business logic
│       ├── issue_service.py     # Issue business logic
│       └── commit_service.py    # Commit business logic
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Error Handling

All GitHub API errors are mapped to meaningful HTTP status codes:

| GitHub status | Connector response | Meaning |
|---|---|---|
| 401 | `401 Unauthorized` | Invalid or missing PAT |
| 403 | `403 Forbidden` | Insufficient token scope |
| 404 | `404 Not Found` | Repo / user / issue doesn't exist |
| 422 | `422 Unprocessable Entity` | Invalid request payload |
| Other | `502 Bad Gateway` | Unexpected GitHub error |

---

## Security Notes

- The PAT is read exclusively from the `GITHUB_PAT` environment variable via `pydantic-settings`.
- `.env` is listed in `.gitignore` — it should **never** be committed.
- The token is sent over HTTPS only (GitHub enforces this).

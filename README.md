# GitHub Cloud Connector

## Prerequisites

- Python 3.11+
- A GitHub Personal Access Token ([create one here by following below steps])
   — Generate a PAT on GitHub

     1. Go to github.com → click your profile picture (top right) → Settings
     2. Scroll down to Developer settings (bottom of left sidebar)
     3. Click Personal access tokens → Tokens (classic)
     4. Click Generate new token → Generate new token (classic)
     5. Fill in:
        Note: github-connector (just a label for yourself)
        Expiration: 30 days / 90 days / No expiration
        Scopes: tick repo (covers everything — public + private repos, issues, etc.)
     6. Click Generate token
     7. Copy it and save it so that we can paste in .env file
 

---

## Setup

```command prompt
# 1. Clone the repository
https://github.com/varshagowdasn/Github-cloud-connector.git
cd Github-Cloud-Connector

# 2. Create and activate a virtual environment
python -m venv virtual_env
source virtual_env\Scripts\Activate       

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
create a file named .env
copy the contents of env.example file and then paste the generated access token(PAT) here.
```

---

## Running the server

```bash
uvicorn app.main:app --reload
```

The API will be available at **http://localhost:8000/docs**.

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
| `GET` | `/issues/{owner}/{repo}/{issue_number}` | Get a specific issue |

**List query parameters**

| Param | Default | Options |
|---|---|---|
| `state` | `open` | `open`, `closed`, `all` |
| `per_page` | `30` | 1–100 |
| `page` | `1` | — |


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
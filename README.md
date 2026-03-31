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
     7. Copy it and save it so that we can paste in .env file later
 

---

## Setup

```command prompt
# 1. Clone the repository
run the command : git clone https://github.com/varshagowdasn/Github-cloud-connector.git
run the command : cd Github-Cloud-Connector

# 2. Create and activate a virtual environment
python -m venv virtual_env
activate using :  virtual_env\Scripts\Activate       

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
create a file named .env
copy the contents of env.example file and then paste the generated access token(PAT) here.
```

---

## Running the server

```command prompt
Inside the Folder Github-Connector run below command :
  uvicorn app.main:app
```

The API will be available at **http://localhost:8000/docs**.

---

## API Endpoints

### Health

| Method | Path | Description |
| `GET` | `/` | Health check |

---

### Repositories — `/repos`

| Method | Path | Description |
| `GET` | `/repos/user/{username}` | List a user's repositories |
| `GET` | `/repos/org/{org}` | List an organisation's repositories |
| `GET` | `/repos/{owner}/{repo}` | Fetch a single repository |


---

### Issues — `/issues`

| Method | Path | Description |
| `GET` | `/issues/{owner}/{repo}` | List issues in a repository |
| `GET` | `/issues/{owner}/{repo}/{issue_number}` | Get a specific issue |


---

### Commits — `/commits`

| Method | Path | Description |
| `GET` | `/commits/{owner}/{repo}` | List commits in a repository |


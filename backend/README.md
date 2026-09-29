# OpenTrade Lab backend

## Run locally

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e '.[test]'
uvicorn opentrade_api.main:app --reload
```

Open `http://localhost:8000/docs` and check `GET /health`.

This service is research-only. It does not execute trades and makes no guaranteed predictions. Live data providers, persistence, authentication, and additional analytics are intentionally added in later milestones.

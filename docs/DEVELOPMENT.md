# Development Guide

## Install

```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS/Linux
source .venv/bin/activate
pip install -r requirements.txt
```

## Start backend

```bash
uvicorn backend.main:app --reload --port 8000
```

## Start frontend

```bash
streamlit run frontend/app.py
```

Frontend: `http://localhost:8501`
API docs: `http://localhost:8000/docs`

## Test

```bash
pytest -q
```

Copy `.env.example` to `.env` for local configuration. Never commit production secrets.

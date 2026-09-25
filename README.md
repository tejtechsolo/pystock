# PyStock — Trading Learning & Analysis OS

Python-first stock-market learning, analysis, risk management, backtesting, paper-trading and guarded broker-integration platform.

> Important: This software is for education, research and hypothetical analysis. It does not provide guaranteed returns or personalized investment advice.

## Architecture
- Frontend: Streamlit (frontend/app.py)
- Backend: FastAPI (backend/main.py)
- Trading/research engine: core/
- Broker connectors: connectors/
- Tests: tests/
- Documentation: docs/

The frontend and backend are both Python. Streamlit provides the interactive UI and FastAPI provides a clean API boundary so the research engine can later support mobile/web clients without coupling UI to trading logic.

## Run locally
python -m venv .venv
Windows: .venv\Scripts\activate
macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt

Start backend: uvicorn backend.main:app --reload --port 8000
Start frontend: streamlit run frontend/app.py
UI: http://localhost:8501
API/OpenAPI: http://localhost:8000/docs
Run tests: pytest -q

## Main capabilities
- Market analysis
- Technical indicators
- Educational backtesting
- Position sizing and risk planning
- Hypothetical profit/loss scenarios
- Trading journal architecture
- Groww connector with live trading disabled by default
- Future stock screener and multi-timeframe analysis
- Future AI tutor and strategy-copilot layer

## LLM policy
The deterministic trading engine does not depend on an LLM. AI will be an optional learning/research layer.
Model usage, selection criteria, governance, and audit requirements are maintained in docs/LLM_MODELS.md and docs/LLM_MODEL_SELECTION.md.
An LLM must never bypass deterministic risk controls or silently place live orders.

## Documentation
- docs/ARCHITECTURE.md — system design
- docs/API.md — API contract
- docs/DEVELOPMENT.md — local development
- docs/SECURITY.md — security and trading safety
- docs/DATA_AND_BACKTESTING.md — research/backtest rules
- docs/LLM_MODELS.md — model registry
- docs/LLM_MODEL_SELECTION.md — model governance
- docs/ROADMAP.md — implementation roadmap

## Environment
Copy .env.example to .env. Never commit real broker/API secrets.
Default safety settings: TRADING_MODE=PAPER and LIVE_TRADING_ENABLED=false.

## Repository
https://github.com/tejtechsolo/pystock
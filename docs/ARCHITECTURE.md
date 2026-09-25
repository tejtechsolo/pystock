# PyStock Architecture

PyStock is a Python-first learning and market-analysis platform for Indian markets.

## Runtime
- Frontend: Streamlit (`frontend/app.py`)
- Backend: FastAPI (`backend/main.py`)
- Research/core engine: `core/`
- Broker/data connectors: `connectors/`
- Tests: `tests/`
- Documentation: `docs/`

## Request flow
Browser → Streamlit → FastAPI → service/core module → market-data provider → normalized response.

## Safety boundary
Live order execution is isolated behind the broker connector and remains disabled unless explicitly configured. Frontend code never stores broker secrets.

## Planned layers
1. API validation/authentication
2. Market-data abstraction and caching
3. Indicator and pattern engine
4. Strategy engine
5. Event-driven backtesting
6. Portfolio/risk engine
7. Paper trading
8. Broker execution
9. AI learning assistant
10. Observability and audit logs

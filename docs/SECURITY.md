# Security

## Secrets
- Keep `.env` local and never commit real credentials.
- Store broker credentials only on the backend/secret manager.
- Streamlit must call backend endpoints and must not contain broker secrets.

## Trading safety
- Live trading is disabled by default.
- Enforce maximum risk per trade, maximum daily loss, and maximum open positions in the backend.
- Require paper-trading validation before any live execution feature is enabled.
- Add idempotency keys and audit logs before live order support.

## API security
Before internet exposure, add authentication, authorization, rate limiting, request-size limits, strict CORS, structured logging, TLS, and dependency scanning.

## AI safety
LLM-generated code is untrusted input. Validate schemas, sandbox execution where required, and never allow an LLM to bypass risk controls.

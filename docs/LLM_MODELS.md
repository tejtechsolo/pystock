# LLM Model Registry

PyStock keeps model usage explicit and auditable. The current trading engine does not require an LLM to calculate indicators, risk, or backtests.

## Current status

| Capability | Model | Status | Purpose |
|---|---|---|---|
| Indicators | None | Active | Deterministic Python calculations |
| Risk calculations | None | Active | Deterministic Python calculations |
| Backtesting | None | Active | Deterministic strategy engine |
| Market data | Provider API | Active | Price/volume data |
| AI tutor | TBD | Planned | Explain concepts and code |
| Research assistant | TBD | Planned | Summarize supplied/retrieved research |
| Strategy copilot | TBD | Planned/guarded | Convert explicit rules into testable code |

## LLM governance
- Never allow an LLM to silently place live orders.
- LLM outputs are advisory and must be validated by deterministic Python.
- Store provider, model identifier, prompt version, timestamp, input context hash, and output status for AI requests.
- Never send broker credentials or unnecessary personal data to an LLM.
- Any AI-generated strategy must pass tests and backtests before paper trading.
- Use a provider abstraction so models can be changed without rewriting trading logic.

## Recommended AI architecture
LLM → structured JSON → schema validation → deterministic strategy/risk engine → human review → paper trading.

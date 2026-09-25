# LLM Model Selection Policy

This is a decision record, not a promise of a particular provider.

## Selection criteria
- Reasoning quality
- Structured-output reliability
- Tool/function calling quality
- Latency
- Cost
- Context-window requirements
- Privacy/data handling
- Availability in the deployment region
- Reproducibility and version stability

## AI roles
### Tutor model
Explanations, quizzes, Python guidance, and trading concepts.

### Research model
Summarize supplied market research and documentation while preserving source references.

### Coding/strategy model
Draft strategy code from explicit rules. Generated code is untrusted until reviewed, tested, and backtested.

### Guardrails
Critical trading controls must remain deterministic Python, not an LLM.

## Versioning
Record provider, model identifier/version, temperature/settings, prompt version, tool schema version, and evaluation result.

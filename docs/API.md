# API Documentation

Base URL: `http://localhost:8000/api`

## Health
GET `/health`

## Market analysis
POST `/market/analyze`

Example request: `{"symbol":"RELIANCE.NS","period":"1y","interval":"1d"}`

Returns the latest OHLCV snapshot and metadata.

## Risk plan
POST `/risk/plan`

Example request: `{"capital":100000,"risk_pct":1,"entry":1000,"stop":980,"target":1040}`

Returns position sizing and hypothetical loss/profit values.

OpenAPI UI: `http://localhost:8000/docs`

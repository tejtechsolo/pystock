from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.routes.health import router as health_router
from backend.api.routes.market import router as market_router
from backend.api.routes.risk import router as risk_router

app = FastAPI(title='PyStock Trading & Learning API', version='0.2.0', description='Educational market analysis, risk, and backtesting API. No investment advice.')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:8501'],
    allow_credentials=False,
    allow_methods=['GET', 'POST'],
    allow_headers=['*'],
)

app.include_router(health_router, prefix='/api')
app.include_router(market_router, prefix='/api')
app.include_router(risk_router, prefix='/api')

@app.get('/')
def root():
    return {'service': 'pystock-api', 'status': 'ok', 'docs': '/docs'}

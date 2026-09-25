from fastapi import APIRouter, HTTPException
import yfinance as yf
from backend.schemas.market import MarketRequest

router = APIRouter(prefix='/market', tags=['market'])

@router.post('/analyze')
def analyze(request: MarketRequest):
    try:
        data = yf.Ticker(request.symbol).history(period=request.period, interval=request.interval, auto_adjust=False)
        if data.empty:
            raise HTTPException(status_code=404, detail='No market data returned for symbol.')
        return {'symbol': request.symbol, 'period': request.period, 'interval': request.interval, 'rows': len(data), 'latest': {
            'timestamp': str(data.index[-1]), 'open': float(data['Open'].iloc[-1]), 'high': float(data['High'].iloc[-1]),
            'low': float(data['Low'].iloc[-1]), 'close': float(data['Close'].iloc[-1]), 'volume': int(data['Volume'].iloc[-1])}}
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f'Market data provider error: {exc}') from exc

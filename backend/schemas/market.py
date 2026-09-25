from pydantic import BaseModel, Field

class MarketRequest(BaseModel):
    symbol: str = Field(min_length=1, max_length=30)
    period: str = '1y'
    interval: str = '1d'

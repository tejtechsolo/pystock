import os
from dotenv import load_dotenv
load_dotenv()
class GrowwConnector:
    def __init__(self): self.token=os.getenv('GROWW_ACCESS_TOKEN',''); self.live_enabled=os.getenv('LIVE_TRADING_ENABLED','false').lower()=='true'; self.client=None
    def connect(self):
        if not self.token: raise RuntimeError('GROWW_ACCESS_TOKEN is not configured.')
        from growwapi import GrowwAPI
        self.client=GrowwAPI(self.token); return self.client
    def holdings(self):
        if not self.client: self.connect()
        return self.client.get_holdings_for_user()
    def positions(self,segment=None):
        if not self.client: self.connect()
        return self.client.get_positions_for_user(segment=segment) if segment else self.client.get_positions_for_user()
    def quote(self,exchange,segment,trading_symbol):
        if not self.client: self.connect()
        return self.client.get_quote(exchange=exchange,segment=segment,trading_symbol=trading_symbol)
    def place_order_guarded(self,**kwargs):
        if not self.live_enabled: raise PermissionError('Live trading is disabled.')
        if not self.client: self.connect()
        return self.client.place_order(**kwargs)

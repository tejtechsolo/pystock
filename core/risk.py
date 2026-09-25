from dataclasses import dataclass
@dataclass
class RiskPlan:
    capital:float; risk_pct:float; entry:float; stop:float; target:float
    @property
    def risk_amount(self): return self.capital*self.risk_pct/100
    @property
    def risk_per_share(self): return abs(self.entry-self.stop)
    @property
    def quantity(self): return int(self.risk_amount//self.risk_per_share) if self.risk_per_share else 0
    @property
    def capital_required(self): return self.quantity*self.entry
    @property
    def potential_loss(self): return self.quantity*self.risk_per_share
    @property
    def potential_profit(self): return self.quantity*abs(self.target-self.entry)
    @property
    def reward_risk(self): return self.potential_profit/self.potential_loss if self.potential_loss else 0
def scenario_profit(capital,return_pct,cost_pct=0): return capital*(return_pct-cost_pct)/100

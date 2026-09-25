from fastapi import APIRouter
from backend.schemas.risk import RiskRequest

router = APIRouter(prefix='/risk', tags=['risk'])

@router.post('/plan')
def risk_plan(request: RiskRequest):
    risk_amount = request.capital * request.risk_pct / 100
    risk_per_share = abs(request.entry - request.stop)
    quantity = int(risk_amount // risk_per_share) if risk_per_share else 0
    capital_required = quantity * request.entry
    potential_loss = quantity * risk_per_share
    potential_profit = quantity * abs(request.target - request.entry)
    rr = potential_profit / potential_loss if potential_loss else 0
    return {'risk_amount': risk_amount, 'risk_per_share': risk_per_share, 'quantity': quantity,
            'capital_required': capital_required, 'potential_loss': potential_loss,
            'potential_profit': potential_profit, 'reward_risk': rr, 'hypothetical': True}

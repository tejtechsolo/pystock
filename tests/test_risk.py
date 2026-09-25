from core.risk import RiskPlan
def test_position_size():
    p=RiskPlan(100000,1,1000,980,1040)
    assert p.quantity==50
    assert p.potential_loss==1000

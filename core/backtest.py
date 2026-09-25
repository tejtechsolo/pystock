def ema_crossover_strategy(df,fast=20,slow=50):
    x=df.copy(); x['fast']=x.Close.ewm(span=fast,adjust=False).mean(); x['slow']=x.Close.ewm(span=slow,adjust=False).mean()
    x['signal']=(x.fast>x.slow).astype(int); x['position']=x.signal.shift(1).fillna(0); x['ret']=x.Close.pct_change().fillna(0)
    x['strategy_ret']=x.position*x.ret; x['equity']=(1+x.strategy_ret).cumprod(); return x
def metrics(bt):
    r=bt.strategy_ret.dropna(); eq=bt.equity; dd=eq/eq.cummax()-1; wins=r[r>0].sum(); losses=abs(r[r<0].sum())
    return {'total_return_pct':(eq.iloc[-1]-1)*100,'max_drawdown_pct':dd.min()*100,'trade_events':int((bt.position.diff().abs()>0).sum()),'profit_factor':wins/losses if losses else float('inf')}

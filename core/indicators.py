import numpy as np
import pandas as pd

def sma(s,n=20): return s.rolling(n).mean()
def ema(s,n=20): return s.ewm(span=n,adjust=False).mean()
def rsi(close,n=14):
    d=close.diff(); gain=d.clip(lower=0); loss=-d.clip(upper=0)
    ag=gain.ewm(alpha=1/n,adjust=False).mean(); al=loss.ewm(alpha=1/n,adjust=False).mean()
    rs=ag/al.replace(0,np.nan); return 100-100/(1+rs)
def macd(close):
    line=ema(close,12)-ema(close,26); signal=ema(line,9); return line,signal,line-signal
def atr(df,n=14):
    p=df['Close'].shift(1); tr=pd.concat([df['High']-df['Low'],(df['High']-p).abs(),(df['Low']-p).abs()],axis=1).max(axis=1)
    return tr.ewm(alpha=1/n,adjust=False).mean()
def add_indicators(df):
    x=df.copy(); x['SMA20']=sma(x.Close,20); x['SMA50']=sma(x.Close,50); x['EMA20']=ema(x.Close,20); x['RSI14']=rsi(x.Close)
    x['MACD'],x['MACD_SIGNAL'],x['MACD_HIST']=macd(x.Close); x['ATR14']=atr(x); return x

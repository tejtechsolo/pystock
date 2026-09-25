import os
import streamlit as st
import pandas as pd
import yfinance as yf
from dotenv import load_dotenv
from core.indicators import add_indicators
from core.risk import RiskPlan, scenario_profit
from core.backtest import ema_crossover_strategy, metrics
from connectors.groww import GrowwConnector

load_dotenv()
st.set_page_config(page_title="Trading Lab",page_icon="📈",layout="wide")
st.title("📈 Trading Lab")
st.caption("Python market analysis, risk, backtesting and Groww workspace")
st.sidebar.info("Mode: "+os.getenv("TRADING_MODE","PAPER"))
st.sidebar.warning("Backtests are hypothetical and are not forecasts or guaranteed profits.")

tabs=st.tabs(["📊 Analyzer","🧪 Backtest","💰 Budget & Risk","📒 Journal","🔗 Groww"])

with tabs[0]:
    st.subheader("Market Analyzer")
    symbol=st.text_input("Yahoo Finance symbol","RELIANCE.NS")
    period=st.selectbox("History",["6mo","1y","2y","5y"],index=1)
    if st.button("Analyze"):
        df=yf.download(symbol,period=period,auto_adjust=False,progress=False)
        if isinstance(df.columns,pd.MultiIndex): df.columns=df.columns.get_level_values(0)
        if df.empty: st.error("No data returned.")
        else:
            df=add_indicators(df.dropna(how="all"))
            c1,c2,c3,c4=st.columns(4)
            c1.metric("Last",f"₹{float(df.Close.iloc[-1]):,.2f}")
            c2.metric("RSI",f"{float(df.RSI14.iloc[-1]):.1f}")
            c3.metric("SMA20",f"₹{float(df.SMA20.iloc[-1]):,.2f}")
            c4.metric("ATR14",f"₹{float(df.ATR14.iloc[-1]):,.2f}")
            st.line_chart(df[["Close","SMA20","SMA50","EMA20"]])
            st.dataframe(df.tail(30),use_container_width=True)

with tabs[1]:
    st.subheader("Educational Backtest")
    symbol2=st.text_input("Backtest symbol","RELIANCE.NS")
    capital=st.number_input("Starting capital (₹)",1000.0,100000000.0,100000.0,5000.0)
    if st.button("Run EMA crossover backtest"):
        df=yf.download(symbol2,period="5y",auto_adjust=False,progress=False)
        if isinstance(df.columns,pd.MultiIndex): df.columns=df.columns.get_level_values(0)
        if df.empty: st.error("No data returned.")
        else:
            bt=ema_crossover_strategy(df.dropna(),20,50); m=metrics(bt)
            a,b,c,d=st.columns(4)
            a.metric("Return",f"{m['total_return_pct']:.2f}%")
            b.metric("Max DD",f"{m['max_drawdown_pct']:.2f}%")
            c.metric("Trade events",m["trade_events"])
            d.metric("Profit factor",f"{m['profit_factor']:.2f}")
            st.line_chart(bt.equity*capital)
            st.caption("Add brokerage, taxes, slippage and liquidity assumptions before treating a backtest as research evidence.")

with tabs[2]:
    st.subheader("Budget, Position Size & Scenario Planner")
    capital=st.number_input("Trading capital (₹)",1000.0,100000000.0,100000.0,5000.0)
    risk_pct=st.slider("Risk per trade (%)",0.1,5.0,1.0,0.1)
    entry=st.number_input("Entry price (₹)",0.01,10000000.0,1000.0)
    stop=st.number_input("Stop price (₹)",0.01,10000000.0,980.0)
    target=st.number_input("Target price (₹)",0.01,10000000.0,1040.0)
    plan=RiskPlan(capital,risk_pct,entry,stop,target)
    c1,c2,c3,c4=st.columns(4)
    c1.metric("Risk budget",f"₹{plan.risk_amount:,.0f}")
    c2.metric("Quantity",f"{plan.quantity:,}")
    c3.metric("Potential loss",f"₹{plan.potential_loss:,.0f}")
    c4.metric("Reward/Risk",f"{plan.reward_risk:.2f}")
    st.write(f"Capital required: ₹{plan.capital_required:,.0f}")
    st.divider()
    st.subheader("Scenario — not a prediction")
    expected=st.slider("Hypothetical return (%)",-50.0,100.0,10.0,1.0)
    costs=st.slider("Assumed total costs (%)",0.0,5.0,0.2,0.05)
    st.metric("Hypothetical P/L",f"₹{scenario_profit(capital,expected,costs):,.0f}")

with tabs[3]:
    st.subheader("Trade Journal")
    st.write("Persistent journal is the next extension: setup, entry, stop, target, result, mistake and lesson.")

with tabs[4]:
    st.subheader("Groww Connection")
    if st.button("Test Groww connection"):
        try:
            data=GrowwConnector().holdings()
            st.success("Groww connection succeeded.")
            st.json(data)
        except Exception as e: st.error(str(e))
    st.warning("Live orders remain blocked unless LIVE_TRADING_ENABLED=true.")

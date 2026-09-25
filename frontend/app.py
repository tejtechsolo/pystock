import os
import requests
import streamlit as st

API_URL = os.getenv('PYSTOCK_API_URL', 'http://localhost:8000/api')
st.set_page_config(page_title='PyStock', page_icon='📈', layout='wide')
st.title('📈 PyStock — Trading Learning & Analysis OS')
st.caption('Educational analytics only. Backtests and profit scenarios are hypothetical.')

tabs = st.tabs(['Market Analyzer', 'Risk Planner', 'Learning', 'System'])

with tabs[0]:
    symbol = st.text_input('NSE/BSE symbol', 'RELIANCE.NS')
    period = st.selectbox('History', ['1mo','3mo','6mo','1y','2y','5y'], index=3)
    interval = st.selectbox('Interval', ['1d','1h','15m','5m'], index=0)
    if st.button('Analyze'):
        try:
            r = requests.post(f'{API_URL}/market/analyze', json={'symbol':symbol,'period':period,'interval':interval}, timeout=20)
            r.raise_for_status()
            st.json(r.json())
        except requests.RequestException as exc:
            st.error(f'Backend unavailable: {exc}')

with tabs[1]:
    capital = st.number_input('Capital (₹)', min_value=1.0, value=100000.0)
    risk_pct = st.number_input('Risk per trade (%)', min_value=0.01, max_value=100.0, value=1.0)
    entry = st.number_input('Entry', min_value=0.01, value=1000.0)
    stop = st.number_input('Stop', min_value=0.01, value=980.0)
    target = st.number_input('Target', min_value=0.01, value=1040.0)
    if st.button('Calculate risk plan'):
        try:
            r = requests.post(f'{API_URL}/risk/plan', json={'capital':capital,'risk_pct':risk_pct,'entry':entry,'stop':stop,'target':target}, timeout=10)
            r.raise_for_status()
            st.json(r.json())
        except requests.RequestException as exc:
            st.error(f'Backend unavailable: {exc}')

with tabs[2]:
    st.subheader('Learning path')
    st.markdown('1. Market structure and order types\n2. Candlesticks and price action\n3. Indicators and market regimes\n4. Risk management and position sizing\n5. Backtesting and statistical validation\n6. Paper trading\n7. Broker integration\n8. Systematic/algorithmic trading')

with tabs[3]:
    st.write('Frontend: Streamlit')
    st.write('Backend: FastAPI')
    st.write('API:', API_URL)
    st.write('Live trading: Disabled by default')

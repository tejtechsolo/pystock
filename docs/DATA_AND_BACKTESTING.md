# Data & Backtesting Rules

Backtests are historical simulations, not forecasts or guarantees.

The production research engine should account for brokerage, STT, exchange transaction charges, GST, SEBI charges, stamp duty, slippage, spread/liquidity, order type, partial fills, corporate actions, market holidays, survivorship bias, and look-ahead bias.

Strategies should be evaluated with out-of-sample and walk-forward testing where appropriate. Parameter optimization must include overfitting controls.

Every backtest run should persist dataset/provider, symbol universe, timeframe, date range, strategy version, parameters, cost assumptions, slippage assumptions, software version, and results.

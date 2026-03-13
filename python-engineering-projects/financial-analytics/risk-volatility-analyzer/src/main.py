import pandas as pd
import yfinance as yf

data = yf.download("AAPL", period="3mo")

returns = data["Close"].pct_change()

volatility = returns.std()

print("Volatility:", volatility)

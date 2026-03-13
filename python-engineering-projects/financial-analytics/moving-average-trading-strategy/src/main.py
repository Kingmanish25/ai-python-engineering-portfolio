import pandas as pd
import yfinance as yf

data = yf.download("AAPL", period="3mo")

data["MA20"] = data["Close"].rolling(window=20).mean()

print(data.tail())

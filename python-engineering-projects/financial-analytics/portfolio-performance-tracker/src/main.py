import pandas as pd

data = {
    "Stock": ["AAPL", "MSFT", "GOOG"],
    "Investment": [1000, 1500, 1200],
    "Current_Value": [1200, 1700, 1400]
}

df = pd.DataFrame(data)

df["Profit"] = df["Current_Value"] - df["Investment"]

print(df)

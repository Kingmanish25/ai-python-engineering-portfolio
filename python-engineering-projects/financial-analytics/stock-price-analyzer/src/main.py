import yfinance as yf

def analyze_stock():

    ticker = yf.Ticker("AAPL")

    data = ticker.history(period="1mo")

    print(data.tail())

if __name__ == "__main__":
    analyze_stock()

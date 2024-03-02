import yfinance as yf
import pandas as pd

# List of ticker symbols for stocks in the S&P 100 index

sp100_tickers = ["AAPL", "MSFT", "AMZN", "GOOGL", "GOOG", "META", "TSLA", "NVDA", "BRK-B", "JPM",
                 "JNJ", "V", "PG", "MA", "UNH", "DIS", "HD", "PYPL", "BAC", "INTC", "CMCSA",
                 "XOM", "NFLX", "VZ", "ADBE", "T", "CRM", "PFE", "ABT", "CVX", "CSCO", "WMT",
                 "PEP", "ABBV", "MRK", "NKE", "KO", "MCD", "HON", "ORCL", "PM", "LIN", "IBM",
                 "AMGN", "QCOM", "MDT", "TXN", "LLY", "NOC", "ACN", "LMT", "SPGI", "NEE",
                 "DHR", "AXP", "BKNG", "UPS", "SBUX", "MMM", "GE", "ISRG", "NOW", "GS", "RTX",
                 "AMD", "BDX", "GILD", "MO", "SCHW", "DE", "LOW", "FIS", "ZTS", "TMO", "ANTM",
                 "CAT", "TFC", "BDX", "BLK", "ICE", "FDX", "TJX", "EMR", "ADI", "CME", "MMC",
                 "COF", "ADP", "SPG", "CHTR", "SYK", "BMY", "VRTX", "CSX", "LRCX"]

# Define the start and end dates for the data
start_date = "2012-01-01"
end_date = "2022-01-01"

# Dictionary to store data for all stocks
sp100_data = {}

# Download data for each stock
for ticker in sp100_tickers:
    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, start=start_date, end=end_date)
    sp100_data[ticker] = data


df = pd.DataFrame({k : v['Close'] for k, v in sp100_data.items()}, index = sp100_data['AAPL'].index)    

df.to_csv("SP100_Close_2012_2022.csv")
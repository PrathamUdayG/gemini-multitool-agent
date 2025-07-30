# tools.pyyfinance
import yfinance as yf
import re

def get_stock_info(query):
    # Naive mapping, improve later with NLP
    if "apple" in query.lower():
        ticker = "AAPL"
    elif "microsoft" in query.lower():
        ticker = "MSFT"
    else:
        match = re.search(r"\b([A-Z]{2,5})\b", query)
        ticker = match.group(1) if match else None

    if not ticker:
        return None

    stock = yf.Ticker(ticker)
    info = stock.history(period="1d")

    if info.empty:
        return "Stock data not available."

    latest_price = info['Close'][-1]
    return f"The latest price of {ticker} is ${latest_price:.2f}"

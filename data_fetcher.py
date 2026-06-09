import yfinance as yf


def fetch_stock_data(symbol):
    data = yf.download(symbol, start="2010-01-01", auto_adjust=True)
    return data

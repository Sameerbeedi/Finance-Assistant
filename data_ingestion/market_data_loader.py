# data_ingestion/market_data_loader.py
import yfinance as yf

def get_stock_data(ticker, period="2d", interval="1d"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period, interval=interval)
    return hist

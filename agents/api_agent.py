# agents/api_agent.py
from yfinance import Ticker

def get_asia_tech_data(ticker="TSM"):
    stock = Ticker(ticker)
    history = stock.history(period="2d")
    return history

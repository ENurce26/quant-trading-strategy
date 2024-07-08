import pandas as pd
import yfinance as yf
from src.strategy import sma_crossover_strategy, backtest_strategy

def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

if __name__ == "__main__":
    data = fetch_stock_data("AAPL", "2015-01-01", "2021-01-01")
    strategy_data = sma_crossover_strategy(data)
    results = backtest_strategy(strategy_data)
    
    print(f"Strategy Results for AAPL:")
    for key, value in results.items():
        print(f"{key}: {value:.4f}")
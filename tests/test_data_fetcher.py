import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import fetch_stock_data
from src.strategy import sma_crossover_strategy, backtest_strategy

def test_fetch_stock_data():
    data = fetch_stock_data("AAPL", "2020-01-01", "2020-01-07")
    assert not data.empty
    assert len(data) > 0

def test_sma_crossover_strategy():
    data = fetch_stock_data("AAPL", "2020-01-01", "2021-01-01")
    strategy_data = sma_crossover_strategy(data)
    assert 'Signal' in strategy_data.columns

def test_backtest_strategy():
    data = fetch_stock_data("AAPL", "2020-01-01", "2021-01-01")
    strategy_data = sma_crossover_strategy(data)
    results = backtest_strategy(strategy_data)
    assert 'Total Return' in results
    assert 'Sharpe Ratio' in results
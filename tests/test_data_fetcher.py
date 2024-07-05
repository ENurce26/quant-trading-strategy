import pytest
from src.main import fetch_stock_data

def test_fetch_stock_data():
    data = fetch_stock_data("AAPL", "2020-01-01", "2020-01-07")
    assert not data.empty
    assert len(data) > 0
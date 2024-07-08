import pandas as pd
import numpy as np

def calculate_sma(data, window):
    return data['Close'].rolling(window=window).mean()

def sma_crossover_strategy(data, short_window=50, long_window=200):
    data['Short_SMA'] = calculate_sma(data, short_window)
    data['Long_SMA'] = calculate_sma(data, long_window)
    
    data['Signal'] = 0
    data.loc[data['Short_SMA'] > data['Long_SMA'], 'Signal'] = 1
    data.loc[data['Short_SMA'] < data['Long_SMA'], 'Signal'] = -1
    
    return data

def backtest_strategy(data):
    data['Returns'] = data['Close'].pct_change()
    data['Strategy_Returns'] = data['Signal'].shift(1) * data['Returns']
    
    cumulative_returns = (1 + data['Strategy_Returns']).cumprod()
    total_return = cumulative_returns.iloc[-1] - 1
    sharpe_ratio = np.sqrt(252) * data['Strategy_Returns'].mean() / data['Strategy_Returns'].std()
    
    return {
        'Total Return': total_return,
        'Sharpe Ratio': sharpe_ratio
    }
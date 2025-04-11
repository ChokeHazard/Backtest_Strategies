import pandas as pd
import numpy as np
import yfinance as yf

def load_yahoo_finance(ticker, interval='1d', period='2y'):
    """
    Load data from Yahoo Finance
    
    Parameters:
    -----------
    ticker : str
        Ticker symbol
    interval : str
        Data interval (1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo)
    period : str
        Data period (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with OHLCV data
    """
    return yf.download(ticker, interval=interval, period=period)

def load_multiple_timeframes(ticker, timeframes=None):
    """
    Load data for multiple timeframes
    
    Parameters:
    -----------
    ticker : str
        Ticker symbol
    timeframes : list
        List of timeframes to load, e.g. ['1h', '1d']
        
    Returns:
    --------
    dict
        Dictionary with timeframes as keys and DataFrames as values
    """
    if timeframes is None:
        timeframes = ['1h', '1d']
    
    data = {}
    for tf in timeframes:
        data[tf] = load_yahoo_finance(ticker, interval=tf)
    
    return data

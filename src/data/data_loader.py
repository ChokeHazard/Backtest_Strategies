import pandas as pd
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
    # Set group_by='ticker' to False to avoid having ticker as column names
    data = yf.download(ticker, interval=interval, period=period, group_by='ticker', auto_adjust=True)

    # Handle MultiIndex in columns (happens with intraday data)
    if isinstance(data.columns, pd.MultiIndex):
        # Convert MultiIndex columns to flat columns
        data.columns = [col[1] for col in data.columns]

    # Ensure we have the required columns for backtesting
    required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
    if not all(col in data.columns for col in required_columns):
        # Try to rename columns if they have different names
        if len(data.columns) >= 5:
            # Assume the first 5 columns are OHLCV in that order
            data.columns = required_columns[:len(data.columns)]

    # Ensure the index is a DatetimeIndex
    if not isinstance(data.index, pd.DatetimeIndex):
        data.index = pd.to_datetime(data.index)

    return data

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

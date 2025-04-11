import pandas as pd
import numpy as np
import yfinance as yf
from backtesting import Backtest, Strategy
from backtesting.lib import crossover

# Load SPX data for backtesting for hourly and daily (D) timeframes
def download_data():
    spx_1h = yf.download('^GSPC', interval='1h', period='2y')
    spx_daily = yf.download('^GSPC', interval='1d', period='2y')
    return spx_1h, spx_daily

class VWMABandsStrategy(Strategy):
    vwma_length_mid = 105
    vwma_length_lower = 105
    vwma_length_upper = 105
    vwma_multiplier_lower = 2.2
    vwma_multiplier_upper = 2.2

    def init(self):
        # Calculate VWMA for mid, lower, and upper bands
        self.vwma_mid = self.I(self.vwma, self.data.Close, self.vwma_length_mid)
        self.vwma_lower_mid = self.I(self.vwma, self.data.Close, self.vwma_length_lower)
        self.vwma_upper_mid = self.I(self.vwma, self.data.Close, self.vwma_length_upper)
        
        self.vwma_std_dev_lower = self.I(self.std_dev, self.data.Close, self.vwma_length_lower, self.vwma_multiplier_lower)
        self.vwma_std_dev_upper = self.I(self.std_dev, self.data.Close, self.vwma_length_upper, self.vwma_multiplier_upper)

        self.vwma_lower_band = self.vwma_lower_mid - self.vwma_std_dev_lower
        self.vwma_upper_band = self.vwma_upper_mid + self.vwma_std_dev_upper

    def vwma(self, close, length):
        if len(close) < length:
            return np.array([np.nan] * len(close))
        weights = np.arange(1, length + 1)
        vwma = np.convolve(close, weights / weights.sum(), mode='valid')
        vwma_full = np.concatenate((np.full(length - 1, np.nan), vwma))
        return vwma_full[-len(close):]

    def std_dev(self, close, length, multiplier):
        close_series = pd.Series(close)
        return close_series.rolling(window=length).std().to_numpy() * multiplier

    def next(self):
        # Long entry condition
        if self.data.Close[-1] < self.vwma_lower_band[-1] and self.data.High[-1] < self.vwma_lower_band[-1]:
            self.buy()

        # Long exit condition
        if (self.data.Close[-1] > self.vwma_upper_band[-1] and self.data.Low[-1] > self.vwma_upper_band[-1]) or (
                self.position and self.data.Close[-1] < self.vwma_upper_band[-1] and self.data.High[-1] < self.vwma_upper_band[-1]
                and self.position.pl_pct > 0):
            self.sell()

if __name__ == "__main__":
    spx_1h, spx_daily = download_data()
    
    # Backtest on daily timeframe as an example
    bt = Backtest(spx_daily, VWMABandsStrategy, cash=10000, commission=.002)
    stats = bt.run()
    
  
   
    bt.plot()

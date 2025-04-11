import argparse
from backtesting import Backtest

from src.data.data_loader import load_multiple_timeframes
from src.strategies.vwma_strategy import VWMABandsStrategy
from src.utils.plot_utils import save_backtest_plot
from src.utils.results_utils import save_backtest_results

def run_backtest(ticker, strategy, timeframes=None, cash=10000, commission=0.002):
    """
    Run backtest for a given ticker and strategy
    
    Parameters:
    -----------
    ticker : str
        Ticker symbol
    strategy : Strategy
        Strategy class
    timeframes : list
        List of timeframes to backtest
    cash : float
        Initial cash
    commission : float
        Commission rate
    """
    if timeframes is None:
        timeframes = ['1h', '1d']
    
    # Load data for multiple timeframes
    data = load_multiple_timeframes(ticker, timeframes)
    
    # Run backtest for each timeframe
    for tf, df in data.items():
        print(f"\nRunning backtest for {ticker} on {tf} timeframe...")
        
        # Create and run backtest
        bt = Backtest(df, strategy, cash=cash, commission=commission)
        stats = bt.run()
        
        # Print backtest results
        print(stats)
        
        # Save backtest results
        results_path = save_backtest_results(stats, strategy.__name__, tf)
        print(f"Results saved to: {results_path}")
        
        # Save backtest plot
        plot_path = save_backtest_plot(bt, strategy.__name__, tf)
        print(f"Plot saved to: {plot_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run backtest for a given ticker and strategy')
    parser.add_argument('--ticker', type=str, default='^GSPC', help='Ticker symbol')
    parser.add_argument('--timeframes', type=str, nargs='+', default=['1h', '1d'], 
                        help='List of timeframes to backtest')
    parser.add_argument('--cash', type=float, default=10000, help='Initial cash')
    parser.add_argument('--commission', type=float, default=0.002, help='Commission rate')
    
    args = parser.parse_args()
    
    # Run backtest with VWMA strategy
    run_backtest(args.ticker, VWMABandsStrategy, args.timeframes, args.cash, args.commission)

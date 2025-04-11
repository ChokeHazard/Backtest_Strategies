import os
import matplotlib.pyplot as plt
from datetime import datetime

def save_backtest_plot(bt, strategy_name, timeframe, plot_dir='plots'):
    """
    Save backtest plot to file
    
    Parameters:
    -----------
    bt : Backtest
        Backtest object
    strategy_name : str
        Name of the strategy
    timeframe : str
        Timeframe of the data
    plot_dir : str
        Directory to save plots
    """
    # Create plots directory if it doesn't exist
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{strategy_name}_{timeframe}_{timestamp}.html"
    filepath = os.path.join(plot_dir, filename)
    
    # Save plot
    bt.plot(filename=filepath, open_browser=False)
    
    return filepath

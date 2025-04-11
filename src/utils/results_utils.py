import os
import json
import pandas as pd
from datetime import datetime

def save_backtest_results(stats, strategy_name, timeframe, results_dir='results'):
    """
    Save backtest results to file
    
    Parameters:
    -----------
    stats : Series
        Backtest statistics
    strategy_name : str
        Name of the strategy
    timeframe : str
        Timeframe of the data
    results_dir : str
        Directory to save results
    """
    # Create results directory if it doesn't exist
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    
    # Generate filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{strategy_name}_{timeframe}_{timestamp}.json"
    filepath = os.path.join(results_dir, filename)
    
    # Convert stats to dict and save as JSON
    stats_dict = stats.to_dict()
    
    # Handle non-serializable objects
    for key, value in stats_dict.items():
        if isinstance(value, pd.DataFrame):
            stats_dict[key] = value.to_dict()
        elif not isinstance(value, (str, int, float, bool, list, dict, type(None))):
            stats_dict[key] = str(value)
    
    with open(filepath, 'w') as f:
        json.dump(stats_dict, f, indent=4)
    
    return filepath

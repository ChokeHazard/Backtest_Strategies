"""
Configuration settings for the backtesting application
"""

# Default settings
DEFAULT_TICKER = '^SPX'  # S&P 500
DEFAULT_TIMEFRAMES = ['1h', '1d']
DEFAULT_CASH = 10000
DEFAULT_COMMISSION = 0.002

# Paths
PLOTS_DIR = 'plots'
RESULTS_DIR = 'results'

# Strategy parameters
VWMA_STRATEGY = {
    'vwma_length_mid': 105,
    'vwma_length_lower': 105,
    'vwma_length_upper': 105,
    'vwma_multiplier_lower': 2.2,
    'vwma_multiplier_upper': 2.2
}

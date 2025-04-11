# Backtesting Application

A modular application for backtesting trading strategies.

## Project Structure

```
backtest_strategies/
├── config/             # Configuration files
├── main.py             # Main entry point
├── plots/              # Generated plots
├── results/            # Backtest results
├── src/                # Source code
│   ├── data/           # Data loading modules
│   ├── strategies/     # Trading strategies
│   └── utils/          # Utility functions
└── tests/              # Unit tests
```

## Getting Started

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run a backtest:
```
python main.py --ticker "^GSPC" --timeframes 1h 1d
```

## Available Strategies

- VWMA Bands Strategy: A strategy based on Volume Weighted Moving Average bands

## Adding New Strategies

To add a new strategy:

1. Create a new file in the `src/strategies/` directory
2. Implement your strategy class extending the `Strategy` class from the `backtesting` package
3. Import your strategy in `main.py` and use it in the `run_backtest` function

## Data Sources

The application currently supports loading data from:

- Yahoo Finance (via yfinance)

To add a new data source, implement a new loader function in the `src/data/` directory.

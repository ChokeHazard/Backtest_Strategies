# Backtesting Application

A modular application for backtesting trading strategies.

## Project Structure

```
backtest_strategies/
├── config/             # Configuration files
├── main.py             # Main entry point
├── plots/              # Generated plots
├── pyproject.toml      # Project metadata and dependencies
├── results/            # Backtest results
├── setup_env.ps1       # Script to set up environment (Windows)
├── setup_env.sh        # Script to set up environment (Unix)
├── src/                # Source code
│   ├── data/           # Data loading modules
│   ├── strategies/     # Trading strategies
│   └── utils/          # Utility functions
└── tests/              # Unit tests
```

## Getting Started

### Using uv (Recommended)

[uv](https://github.com/astral-sh/uv) is a fast Python package installer and resolver. To set up the project with uv:

1. Install uv if you don't have it already:
```
pip install uv
```

2. Set up the environment using the provided script:

On Windows:
```
.\setup_env.ps1
```

On Unix-based systems:
```
chmod +x setup_env.sh
./setup_env.sh
```

3. Activate the virtual environment:

On Windows:
```
.venv\Scripts\Activate.ps1
```

On Unix-based systems:
```
source .venv/bin/activate
```

### Using pip (Alternative)

1. Create and activate a virtual environment:
```
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows
source .venv/bin/activate    # Unix
```

2. Install the package in development mode:
```
pip install -e .
```

### Running the Application

#### Using uv run (Recommended)

With uv, you can run the application without activating the virtual environment:

```
uv run python main.py --ticker "^GSPC" --timeframes 1h 1d
```

You can also use uv run to execute other Python scripts or commands:

```
# Run a specific script
uv run python src/some_script.py

# Run development tools
uv run black src/
uv run isort src/
uv run flake8 src/
uv run pytest
```

#### Using python directly

If you've activated the virtual environment, you can also run the application directly:

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

## Development with uv

### Managing Dependencies

To add new dependencies to the project:

```
# Add a runtime dependency
uv pip install package_name

# Add a development dependency
uv pip install package_name --dev
```

After adding dependencies, update the pyproject.toml file to include them:

```toml
# For runtime dependencies
dependencies = [
    # existing dependencies...
    "package_name>=version",
]

# For development dependencies
[project.optional-dependencies]
dev = [
    # existing dev dependencies...
    "package_name>=version",
]
```

### Updating Dependencies

To update all dependencies to their latest versions:

```
uv pip sync --upgrade
```

To update a specific package:

```
uv pip install --upgrade package_name
```

### Exporting Dependencies

To export the current environment's dependencies to a requirements.txt file:

```
uv pip freeze > requirements.txt
```

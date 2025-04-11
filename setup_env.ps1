# PowerShell script to set up a virtual environment using uv

# Create a virtual environment
Write-Host "Creating virtual environment with uv..." -ForegroundColor Green
uv venv

# Activate the virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Green
& .\.venv\Scripts\Activate.ps1

# Install dependencies from pyproject.toml
Write-Host "Installing dependencies..." -ForegroundColor Green
uv pip install -e .

# Install development dependencies
Write-Host "Installing development dependencies..." -ForegroundColor Green
uv pip install -e ".[dev]"

Write-Host "Virtual environment setup complete!" -ForegroundColor Green
Write-Host "You can activate the environment with: .\.venv\Scripts\Activate.ps1" -ForegroundColor Yellow

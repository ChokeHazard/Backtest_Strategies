#!/bin/bash
# Bash script to set up a virtual environment using uv

# Create a virtual environment
echo -e "\033[0;32mCreating virtual environment with uv...\033[0m"
uv venv

# Activate the virtual environment
echo -e "\033[0;32mActivating virtual environment...\033[0m"
source .venv/bin/activate

# Install dependencies from pyproject.toml
echo -e "\033[0;32mInstalling dependencies...\033[0m"
uv pip install -e .

# Install development dependencies
echo -e "\033[0;32mInstalling development dependencies...\033[0m"
uv pip install -e ".[dev]"

echo -e "\033[0;32mVirtual environment setup complete!\033[0m"
echo -e "\033[0;33mYou can activate the environment with: source .venv/bin/activate\033[0m"

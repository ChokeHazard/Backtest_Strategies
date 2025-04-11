"""
This setup.py file is provided for backward compatibility with tools that don't support pyproject.toml.
For modern Python packaging, we recommend using pyproject.toml and build tools like uv.
"""

from setuptools import setup, find_packages

setup(
    name="backtest-strategies",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.9",
)

# Financial Portfolio Optimization & Data Pipeline

## Objective

Build a data pipeline and investment analysis tool that automates the extraction of financial data, stores it in a structured SQL database, and applies Modern Portfolio Theory (MPT) to recommend optimal asset allocation based on risk profiles.

## Tech Stack

- **Language:** Python (Pandas, NumPy, SciPy)
- **Database:** SQL (SQLite)
- **API:** Yahoo Finance (yfinance)
- **Visualization:** Power BI, Plotly / Matplotlib
- **Environment:** VS Code / Anaconda

## Architecture

The pipeline follows a structured flow: raw financial data is extracted via API, cleaned and transformed in Python, stored in a relational SQL database, and then connected to Power BI for interactive visualization and risk/return analysis.

## Status

Actively in development — this project is being built as a real tool for use in investment advisory work, not only as a portfolio demonstration.

## Data Source

Financial data sourced via [Yahoo Finance API](https://pypi.org/project/yfinance/) (yfinance).

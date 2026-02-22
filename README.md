# Financial Portfolio Optimization & Data Pipeline

## 1. Project Objective
The goal of this project is to build a professional-grade data pipeline and investment tool. It automates the extraction of financial data, stores it in a structured SQL database, and applies Modern Portfolio Theory (MPT) to recommend optimal asset allocation based on risk profiles.

## 2. Tech Stack
* **Language:** Python (Pandas, NumPy, Scipy)
* **Database:** SQL (SQLite)
* **API:** Yahoo Finance (yfinance)
* **Visualization:** Plotly / Matplotlib / Power BI
* **Environment:** VS Code / Anaconda

## 3. Data Model


## 4. Project Roadmap

Phase 1: Infrastructure and Setup
[x] Create directory structure (data, src, sql, notebooks, dashboard).
[x] Create .gitignore file to protect local data and temporary files.
[x] Create requirements.txt file listing all necessary Python dependencies.

Phase 2: Data Extraction and Transformation (Python ETL)
[x] Develop src/etl.py script to automate financial data download via yfinance.
[x] Filter and clean data for the 6 selected assets (handle missing values, standardize dates).
[x] Save backup CSV files in data/raw (raw data) and data/processed (clean data).

Phase 3: Data Modeling and Storage (SQL)
[ ] Design relational database schema and save it to sql/schema.sql.
[ ] Develop src/database.py script to initialize the local database (SQLite).
[ ] Insert processed data from the Python ETL pipeline into SQL tables.

Phase 4: Exploratory and Quantitative Analysis (EDA in Notebook)
[ ] Create 01_exploratory_analysis.ipynb notebook.
[ ] Establish connection between the notebook and the SQL database.
[ ] Calculate essential financial metrics (Daily Returns, Volatility, and Correlation Matrix).
[ ] Validate business logic and quantitative models before building the dashboard.

Phase 5: Data Visualization (Power BI)
[ ] Connect Power BI directly to the SQLite database.
[ ] Create required DAX measures for financial tracking.
[ ] Develop an interactive dashboard (Market Overview, Asset Correlation, and Risk/Return profiles).
[ ] Save the final .pbix file in the dashboard/ directory.

Phase 6: Documentation and Delivery (GitHub)
[ ] Write a comprehensive README.md (Project goals, architecture overview, and business insights).
[ ] Commit and push the finalized project to the remote GitHub repository.
# Here we extract, transform, and load data (ETL).
# This is a "Full Load" script, which means every time it runs, it overwrites the existing .csv.
# It does not append new information. Therefore, it is idempotent and safe to run multiple times.

# Libraries
import yfinance as yf
import pandas as pd
import os

# Define the function and its parameters


def run_etl(lista_ativos, periodo='5y'):

    # The 'os' library is used to manage directory paths.
    # exist_ok=True ensures the code doesn't crash if the directory already exists.
    os.makedirs('../data/raw', exist_ok=True)
    os.makedirs('../data/processed', exist_ok=True)

    # --- EXTRACT ---
    print(f"Extraindo dados de {len(lista_ativos)} ativos...")

    # yfinance downloads the data. We use 'Adj Close' because it accounts for dividend payouts and stock splits.
    # The output is natively returned as a Pandas DataFrame.
    df_raw = yf.download(lista_ativos, period=periodo, progress=False)['Close']

    # .to_csv exports the raw dataframe into a .csv file. This is our raw data backup for security and governance.
    df_raw.to_csv('../data/raw/historico_bruto.csv')
    print("Dados brutos salvos em '../data/raw/historico_bruto.csv'.")

    # --- TRANSFORM ---
    print("Iniciando transformação dos dados...")

    # Step A: .reset_index() moves the Date from the index into a standard column.
    df_clean = df_raw.reset_index()

    # Step B: The Unpivot (Melt).
    # SQL and Power BI work best with long tables rather than wide tables.
    # .melt() transforms the wide table: 'Date' remains fixed, tickers go into a single 'Ticker' column, and prices into 'Preco_Ajustado'.
    df_clean = df_clean.melt(
        id_vars=['Date'], var_name='Ticker', value_name='Preco_Ajustado')

    # Step C: .dropna() removes NaN (Not a Number) values, which occur on weekends/holidays when the market is closed.
    df_clean = df_clean.dropna()

    # Step D: .round(2) standardizes the prices to 2 decimal places (standard financial format).
    df_clean['Preco_Ajustado'] = df_clean['Preco_Ajustado'].round(2)

    #Calculate Daily Return (Upstream Processing for Power BI)
    # 1. Sort by Ticker and Date to ensure correct chronological order
    df_clean = df_clean.sort_values(by=['Ticker', 'Date'])
    # 2. Calculate percentage change
    df_clean['Retorno_Diario'] = df_clean.groupby('Ticker')['Preco_Ajustado'].pct_change()
    # 3. Fill the first day's NaN with 0, and round to 4 decimal places (e.g., 0.0150 for 1.5%)
    df_clean['Retorno_Diario'] = df_clean['Retorno_Diario'].fillna(0).round(4)

    # --- LOAD ---
    # index=False prevents Pandas from exporting an unnecessary sequential numeric column.
    df_clean.to_csv('../data/processed/historico_processado.csv', index=False)
    print("Dados processados salvos em '../data/processed/historico_processado.csv'.")
    print("ETL concluído com sucesso!")


# This block ensures the script only runs if executed directly, not when imported by another file.
if __name__ == "__main__":
    # Choose the assets you want to explore and the historical timeframe.
    meus_ativos = ['BTC-USD', 'BTLG11.SA', 'AAPL34.SA', 'PETR4.SA', 'LFTS11.SA', 'GOLD11.SA', '^BVSP', '^GSPC', 'B5P211.SA']
    periodo_escolhido = '5y'

    # Pass the variables into the function
    run_etl(lista_ativos=meus_ativos, periodo=periodo_escolhido)

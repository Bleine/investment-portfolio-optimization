# here we are going to populeted the tables with the values in the .csv with python.

# libraries
import pandas as pd  # manipulates the .csv
import sqlite3  # talks to the database


def load_data_to_db():
    # open the connection with the .db
    conn = sqlite3.connect('../data/processed/portfolio.db')
    cursor = conn.cursor()  # executes the commands inside of the .db
    # upload the data as da DataFrame
    df = pd.read_csv('../data/processed/historico_processado.csv')

    unique_tickers = df['Ticker'].unique()  # select only once each ticker

    for ticker in unique_tickers:
        cursor.execute(
            "INSERT OR IGNORE INTO dim_assets (ticker, sector) VALUES (?, ?)", (ticker, 'N/A'))
        conn.commit()  # just save when all had run.

    cursor.execute('SELECT id_assets, ticker FROM dim_assets')
    # row[1] is a text and row [0] is the number
    dim_assets_map = {row[1]: row[0] for row in cursor.fetchall()}
    # .map uses the ticker column to create a new one with numbers('id_assets')
    df['id_assets'] = df['Ticker'].map(dim_assets_map)

    df_fact = df[['id_assets', 'Date', 'Preco_Ajustado']].copy()
    # change name of the columns
    df_fact.rename(
        columns={'Date': 'date', 'Preco_Ajustado': 'adj_close'}, inplace=True)
    # .to_sql get the values of Pandas and insert into tables
    df_fact.to_sql('fact_prices', conn, if_exists='append', index=False)

    conn.close()


if __name__ == "__main__":
    load_data_to_db()

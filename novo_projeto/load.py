import pandas as pd
import sqlite3


def load():
    dados = pd.read_csv('dados_limpos.csv')
    conn = sqlite3.connect('ativos.db')
    dados = dados.reset_index()
    dados.to_sql('ativos', conn, if_exists='replace', index=False)
    conn.close()


if __name__ == '__main__':
    load()

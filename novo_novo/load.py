import pandas as pd
import sqlite3
from datetime import datetime


def load():
    # 1. Carregar os dados
    dados = pd.read_csv('dados_limpos.csv')

    # Pegamos os tickers únicos
    ativos_unicos = dados['Ticker'].unique()

    # 2. Conectar ao Banco e Criar Tabelas
    conn = sqlite3.connect('dados_ativos.db')
    cursor = conn.cursor()

    # exclui as tabelas
    cursor.execute('DROP TABLE IF EXISTS dados_ativos')
    cursor.execute('DROP TABLE IF EXISTS ativos')
    conn.commit()

    with open('tabelas.sql', 'r') as tabelas:
        queries = tabelas.read()
    cursor.executescript(queries)
    conn.commit()

    for ticker in ativos_unicos:

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('INSERT INTO ativos (ativo, created_at) VALUES (?, ?)',
                       (ticker, now)
                       )
    conn.commit()

    for dados_ativos in dados.iloc:
        item_name = dados_ativos['Ticker']
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        ticker_id = cursor.execute(
            "SELECT id FROM ativos WHERE ativo = ? LIMIT 1",
            (item_name,)
        )
        cursor.execute(
            'INSERT INTO dados_ativos (id_ativos, data_negociacao, preco_ajustado, retorno_diario, created_at) VALUES (?, ?, ?, ?, ?)',
            (ticker_id.fetchone()[0], dados_ativos['Date'], dados_ativos['Preço Ajustado'], dados_ativos['Retorno Diário'], now))

    conn.commit()
    conn.close()

import sqlite3
import pandas as pd


def testar_banco_final():
    # 1. Abre a porta do banco de dados
    conn = sqlite3.connect('../data/processed/portfolio.db')

    # 2. Traz a tabela de Cadastro (Agora com os Setores!)
    print("=== TABELA ATIVOS (dim_assets) ===")
    df_ativos = pd.read_sql("SELECT * FROM dim_assets", conn)
    print(df_ativos)

    # 3. Traz uma amostra da tabela Fato
    print("\n=== TABELA PRECOS (fact_prices) - Primeiras 10 linhas ===")
    df_precos = pd.read_sql("SELECT * FROM fact_prices LIMIT 10", conn)
    print(df_precos)

    # 4. Fecha a porta
    conn.close()


if __name__ == "__main__":
    testar_banco_final()

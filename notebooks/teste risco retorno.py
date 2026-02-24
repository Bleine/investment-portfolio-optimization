import sqlite3
import pandas as pd
import numpy as np

def analisar_metricas():
    # 1. Abre a conexão com a nossa base de dados
    conn = sqlite3.connect('../data/processed/portfolio.db')

    # 2. A Mágica do SQL Relacional (JOIN)
    # Vamos pegar o nome do ativo (ticker) de uma tabela, e a data e o retorno da outra.
    query = """
        SELECT d.ticker, f.date, f.daily_return
        FROM fact_prices f
        JOIN dim_assets d ON f.id_assets = d.id_assets
    """
    
    # 3. Executa a query e joga no Pandas
    df = pd.read_sql(query, conn)
    conn.close()

    print("Calculando métricas financeiras dos últimos 5 anos...\n")

    # 4. Cálculo da Volatilidade Anualizada (Risco)
    # std() é o desvio padrão diário. Multiplicamos pela raiz de 252 (dias úteis) e por 100 para virar %.
    volatilidade = df.groupby('ticker')['daily_return'].std() * np.sqrt(252) * 100

    # 5. Cálculo do Retorno Acumulado
    # (1 + retorno).prod() - 1 é a fórmula matemática dos juros compostos
    retorno_total = (df.groupby('ticker')['daily_return'].apply(lambda x: (1 + x).prod() - 1)) * 100

    # 6. Criando um relatório bonito (Dataframe Final)
    relatorio = pd.DataFrame({
        'Retorno Acumulado (%)': retorno_total.round(2),
        'Risco / Volatilidade (%)': volatilidade.round(2)
    })

    # Ordena para mostrar quem rendeu mais no topo
    relatorio = relatorio.sort_values(by='Retorno Acumulado (%)', ascending=False)
    
    print("=== RELATÓRIO DE RISCO E RETORNO ===")
    print(relatorio)

if __name__ == "__main__":
    analisar_metricas()
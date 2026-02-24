import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plotar_correlacao():
    print("Conectando ao banco e buscando o histórico de retornos...")
    # 1. Conecta no banco
    conn = sqlite3.connect('../data/processed/portfolio.db')

    # 2. A Mágica do SQL Relacional (JOIN)
    # Trazemos os dados de retornos cruzando com o nome dos ativos
    query = """
        SELECT d.ticker, f.date, f.daily_return
        FROM fact_prices f
        JOIN dim_assets d ON f.id_assets = d.id_assets
    """
    df = pd.read_sql(query, conn)
    conn.close()

    # 3. Transformação Pivot (De Long para Wide)
    # O Seaborn precisa que cada ativo seja uma COLUNA e cada data seja uma LINHA.
    df_pivot = df.pivot(index='date', columns='ticker', values='daily_return')

    print("Calculando a matemática da correlação...")
    # 4. A função matemática que calcula a matriz inteira em 1 segundo:
    matriz_corr = df_pivot.corr()

    # 5. Desenhando o Gráfico (Heatmap)
    print("Gerando o Mapa de Calor...")
    plt.figure(figsize=(10, 8))

    # annot=True (mostra os números), cmap='coolwarm' (cores de temperatura: azul para frio/negativo, vermelho para quente/positivo)
    sns.heatmap(matriz_corr, annot=True, cmap='coolwarm',
                fmt=".2f", vmin=-1, vmax=1, linewidths=0.5)

    plt.title('Matriz de Correlação do Portfólio (Retornos Diários - 5 Anos)',
              fontsize=14, pad=20)

    # 6. Salvar a imagem e mostrar na tela
    plt.tight_layout()
    plt.savefig('heatmap_correlacao.png')  # Salva um PNG na sua pasta
    print("Sucesso! Imagem salva como 'heatmap_correlacao.png'. Abrindo o gráfico...")

    plt.show()  # Abre a janela interativa para você ver agora!


if __name__ == "__main__":
    plotar_correlacao()

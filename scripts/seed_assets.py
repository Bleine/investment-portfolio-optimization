#importa as bibliotecas (sqlite3 faz o python falar com SQL e a os mostra o caminho do DataBase dentro das pastas, independente de quem usa)
import sqlite3
import os

#código para mostrar onde está o banco de dados
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(base_dir, 'data', 'portfolio.db')

try:
    # tuplas para povoar a tabela dim_assets
    assets = [
        ('PETR4.SA', 'Petrobrás', 'Ação BR'),
        ('LFTS11.SA', 'Tesouro Selic ETF', 'Renda Fixa'),
        ('BTLG11.SA', 'BTG Logística', 'FII'),
        ('AAPL', 'Apple Inc', 'Stock US'),
        ('GOLD11.SA', 'Ouro ETF', 'Commodity'),
        ('BTC-USD', 'Bitcoin', 'Cripto')
            ]

    #Conectar e inserir - conn abre a conexão com o .db e o cursor é quem leva o comando até o banco.
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    #.executemany insere os valores mais rápido. INSERT INTO diz em quais colunas os valores devem entrar
    #(?, ?, ?) diz ao banco "espere 3 valores"
    cursor.executemany("""
        INSERT INTO dim_assets (ticker, asset_name, asset_type)
        VALUES (?, ?, ?)
    """, assets)
    #só salva a inserção se não der erro
    conn.commit()
    print("Sucesso!")

except sqlite3.IntegrityError:
    print("Aviso: Esses ativos já existem no banco.")

finally:
    #fecha a conexão
        conn.close()
        print("Conexão encerrada com segurança.")
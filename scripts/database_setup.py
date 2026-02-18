#importa a biblioteca SQLite3, que é nativa de Python
import sqlite3 
#mostra o caminho onde está o Banco de Dados
db_path = 'data/portfolio.db' 
#Usa o método .connect para conectar a biblioteca sqlite3 com o banco de dados
conn = sqlite3.connect(db_path)
# O métido .cursor() é o responsável por fazer com que Pytohn entenda os comandos SQL
cursor = conn.cursor()
print("Banco de dados pronto para receber comandos!")


#Criação de Tabelas. usar o .commit() no final para garantir que a tabela toda foi criada. caso o processamento pare antes, nada é criado.

cursor.execute("""
CREATE TABLE IF NOT EXISTS dim_assets(
    asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticker TEXT NOT NULL UNIQUE,
    asset_name TEXT,
    asset_type TEXT
)
""") 
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_prices(
        price_id INTEGER PRIMARY KEY AUTOINCREMENT,
        asset_id INTEGER NOT NULL,
        date DATE,
        close_price REAL,
        volume INTEGER,
FOREIGN KEY (asset_id) REFERENCES dim_assets (asset_id))
""")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS fact_portfolios(
    portfolio_id INTEGER PRIMARY KEY AUTOINCREMENT,
    risk_profile TEXT,
    asset_id INTEGER, 
    weight REAL,
    FOREIGN KEY (asset_id) REFERENCES dim_assets (asset_id))   
""")
conn.commit()


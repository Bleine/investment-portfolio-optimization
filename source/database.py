#Script que cria as tabelas e salva no SQL

# Libraries
import sqlite3
import os

#a function is used if we wanted runs this code in other times
def create_database():
   
    
    #here are the locations of the .db and the schema.sql, with the tables.
    caminho_banco = '../data/processed/portfolio.db'
    caminho_sql = '../sql/schema.sql'
    
    #here i open the connection - with make sure the connection is colosed after runs the code
    # connection between python and sql is made from the .connect(which file is the .db -if not exist, it will be created) method, called as conn. .cursor is the responsabel for bring the data.
    with sqlite3.connect(caminho_banco) as conn:
        cursor = conn.cursor()
        
        # read the schema.sql. 't' means just read, encoding='uft-8' is to make sure the code runs even if I wrote some special caracter
        
        with open(caminho_sql, 'r', encoding='utf-8') as file:
            #the code read the schema.sql and save in the python memory as a variable script_sql
            script_sql = file.read()
            
        # cursor, who is responsable for brings data, execute the script with the schema of the tables. executescrip() execute all by once.
       
        cursor.executescript(script_sql)
        
    print(f"Sucesso! Banco de dados criado em: {caminho_banco}")

#code for security to this doesn't run alone.
if __name__ == "__main__":
    create_database()
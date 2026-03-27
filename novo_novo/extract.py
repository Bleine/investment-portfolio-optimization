import yfinance as yf
import pandas as pd


def extract():
    ativos_escolhidos = ['AAPL34.SA', '^GSPC', 'WEGE3.SA', 'BBAS3.SA']
    periodo = 'max'

    dados_brutos = yf.download(
        ativos_escolhidos, period=periodo, auto_adjust=False)['Adj Close']
    dados_brutos.to_csv('dados_brutos.csv')
    print('Arquivo .csv criado')


if __name__ == '__main__':
    extract()

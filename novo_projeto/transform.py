import yfinance as yf
import pandas as pd
import numpy as np


def transform():
    dados_brutos = pd.read_csv(
        'dados_brutos.csv', sep=',', decimal='.', index_col=0)
    dados_limpos = dados_brutos.dropna()
    dados_limpos = dados_limpos.reset_index()
    dados_limpos = dados_limpos.melt(
        id_vars=['Date'], var_name='Ticker', value_name='Preço Ajustado')
    dados_limpos['Retorno Diário'] = np.round(dados_limpos.groupby('Ticker')[
                                              'Preço Ajustado'].pct_change()*100, 2)
    dados_limpos = dados_limpos.dropna()
    dados_limpos.to_csv('dados_limpos.csv', index=False)


if __name__ == '__main__':
    transform()

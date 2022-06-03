import pandas as pd
import seaborn as sns

NOME_ARQUIVO_FONTE = 'gasolina.csv'

gasolina = pd.read_csv(NOME_ARQUIVO_FONTE, sep=',', encoding='utf-8')

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=gasolina, x="dia", y="venda", palette="dark")
  grafico.set(title='Venda de gasolina por dia', xlabel='Dia', ylabel='Venda');
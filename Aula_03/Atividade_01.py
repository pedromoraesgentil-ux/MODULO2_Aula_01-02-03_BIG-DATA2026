import pandas as pd
import subprocess
import numpy as np


subprocess.run('cls', shell=True)

df_planilha_moveis =pd.read_csv('planilha_moveis.csv')
print(df_planilha_moveis)

array_custo_moveis=np.array(df_planilha_moveis['Preco'].head())


#Calculando Quartis, média, mediana, minimo e maximo 

minimo=np.min(array_custo_moveis)
maximo=np.max(array_custo_moveis)
mediana=np.median(array_custo_moveis)
media= np.mean(array_custo_moveis)
q1=np.quantile(array_custo_moveis,.25)
q2=np.quantile(array_custo_moveis,.50)
q3=np.quantile(array_custo_moveis,.75)
q4=np.quantile(array_custo_moveis,.100)


#_______________________________________________________________________#

#´PRINT
print(f'O valor minimo é {minimo} -> Esta faixa agrupa os 25% produtos com menor faturamento da empresa. ')
print(f'O valor maximo é {maximo}')
print(f'O valor da média é {media}')
print(f'O valor da médiana é: {mediana}-> O valor que melhor representa o comportamento central do faturamento é a Mediana (Q2).')
print(f'O Terceiro quartil {q3} ->25% produtos que geram maior receita ')
print(f'Q1:{q1}')
print(f'Q2:{q2}')
print(f'Q3:{q3}')
print(f'Q4:{q4}')
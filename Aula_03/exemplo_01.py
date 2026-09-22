import pandas as pd
import subprocess
# pip install numpy
import numpy as np


subprocess.run('cls', shell=True)

df_planilha_custo = pd.read_csv('planilha_de_custos.csv')
print(df_planilha_custo.head(10))

# df * vl_porcentagem / 100
df_planilha_custo['Custo Total (R$)'] = (
    df_planilha_custo['Preco de Compra (R$)'] +
    (df_planilha_custo['Preco de Compra (R$)'] * df_planilha_custo['Imposto (%)'] / 100) +
    df_planilha_custo['Frete (R$)'] +
    df_planilha_custo['Taxa Operacional (R$)']
)

# Impressões
print('\nPlanilha de Custo Total')
print(50 * '-')
print(df_planilha_custo.head())
#_________________________________________________________________________________________________________________________#



print('\nSérie Produtos e Total')
print(50 * '-')
print(df_planilha_custo[['Produto', 'Custo Total (R$)']].head())


# Criando um array de custos
array_custo_total = np.array(df_planilha_custo['Custo Total (R$)'])

media = np.mean(array_custo_total)
mediana = np.median(array_custo_total)
maximo = np.max(array_custo_total)
minimo = np.min(array_custo_total)


print('\nMedidas de Tendência Central')
print(50 * '-')
print(f'Média: {media}')
print(f'Mediana: {mediana}')


#calculando quartis 

q1= np.quantile(array_custo_total,.25)
q2= np.quantile(array_custo_total,.50)
q3= np.quantile(array_custo_total,.75)
q4= np.quantile(array_custo_total,.100)


#Quartis 
print('\nQuartil')
print(50 * '-')
print(f'Menor custo: {minimo}')
#print(f'Q1:{q1}')
print(f'Q2:{q2}')
print(f'Q3:{q3}')
#print(f'Q4:{q4}')
print(f'Maior custo: {maximo }')













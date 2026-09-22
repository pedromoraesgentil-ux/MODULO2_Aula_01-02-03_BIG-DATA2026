import pandas as pd
import subprocess
# pip install numpy
import numpy as np

subprocess.run('cls', shell=True)

df_planilha_vendas =pd.read_excel('vendas_ubá.xlsx')
print(df_planilha_vendas)

#criando um array de custos 
array_vendas= np.array(df_planilha_vendas['Valor'])

media = np.mean(array_vendas)
mediana= np.median(array_vendas)
maximo=np.max(array_vendas)
minimo= np.min(array_vendas)
total = np.sum(array_vendas)

print('\nMedidas de Tendência Central')
print(50 * '-')
print(f'Média: {media}')
print(f'Mediana: {mediana}')


#calculando quartis 

q1= np.quantile(array_vendas,.25)
q2= np.quantile(array_vendas,.50)
q3= np.quantile(array_vendas,.75)
q4= np.quantile(array_vendas,.99)

#Quartis 
print('\nQuartil')
print(50 * '-')
print(f'Menor custo: {minimo}')
print(f'Q1:{q1}')
print(f'Q2:{q2}')
print(f'Q3:{q3}')
print(f'Q4:{q4}')
print(f'Maior custo: {maximo }')
print(f'Total{total}')


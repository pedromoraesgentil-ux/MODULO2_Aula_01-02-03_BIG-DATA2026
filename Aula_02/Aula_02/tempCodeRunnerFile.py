import pandas as pd
import subprocess
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

print('\nSérie Produtos e Total')
print(50 * '-')
print(df_planilha_custo[['Produto', 'Custo Total (R$)']].head())


#Array de custos 

array_custo_total = np.array(df_planilha_custo[df_planilha_custo['Custo Total (R$)']])

media = np.mean(array_custo_total)
mediana= np.median(array_custo_total)

print('\nMedids de Tendência Central')
print(50*"_")
print(f'print{media}')
print(f'{mediana}')

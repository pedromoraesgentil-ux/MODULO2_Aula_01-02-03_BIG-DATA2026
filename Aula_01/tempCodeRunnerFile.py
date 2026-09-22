import pandas as pd

df_vendas= pd.read_excel('vendas_eletronicos.xlsx')
#print(df_vendas)

print(df_vendas.head())

#maior faturamento
print("\nMaior Faturamento")
maximo= df_vendas[f'O Faturameto total (R$)'].max()
print(def_vendas[def_vendas['O Faturameto total (R$)'] == maximo][['Produto','Faturamento Total (R$)']])

#Menor faturamento
print('\nMenor Faturamento')
minimo= df_vendas['O faturameto total (R$)'].min()
print(df_vendas[def_vendas['O faturameto total (R$)'] == minimo][['Produto','Faturamento Total (R$)']])







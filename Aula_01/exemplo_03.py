import pandas as pd

df_vendas= pd.read_excel('vendas_eletronicos.xlsx')
#print(df_vendas)

print(df_vendas.head())

#maior faturamento
print("\nMaior Faturamento")
maximo= df_vendas[f'Faturamento Total (R$)'].max()
print(df_vendas[df_vendas['Faturamento Total (R$)'] == maximo][['Produto','Faturamento Total (R$)']])

#Menor faturamento
print('\nMenor Faturamento')
minimo= df_vendas['Faturamento Total (R$)'].min()
print(df_vendas[df_vendas['Faturamento Total (R$)'] == minimo][['Produto','Faturamento Total (R$)']])







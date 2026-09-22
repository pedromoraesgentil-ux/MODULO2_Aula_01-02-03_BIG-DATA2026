import pandas as pd

df_vendas = pd.read_excel('vendas_eletronicos.xlsx')
print(df_vendas.head())

# maior valor
# print('')
print(f'\nMaior Faturamento:')
maximo = df_vendas['Faturamento Total (R$)'].max()
print(df_vendas[df_vendas['Faturamento Total (R$)'] == maximo][['Produto', 'Faturamento Total (R$)']])


print(f'\nMenor Faturamento:')
print(f'Menor Faturamento: R$ {df_vendas['Faturamento Total (R$)'].min()}')
menor = df_vendas['Faturamento Total (R$)'].min()
print(df_vendas[df_vendas['Faturamento Total (R$)'] == menor][['Produto', 'Faturamento Total (R$)']])


print(f'\nQuantidade Total de Unidades Vendidas: R$ {df_vendas['Unidades Vendidas'].sum()}')
print(f'Preço Médio dos Produtos: R$ {df_vendas['Preco por Unidade (R$)'].mean()}')

# méida das undiades vendidas
media = df_vendas['Unidades Vendidas'].mean()
print(f'\nMédia de Unidades Vendidas: {media}')
print(df_vendas[df_vendas['Unidades Vendidas'] < media])



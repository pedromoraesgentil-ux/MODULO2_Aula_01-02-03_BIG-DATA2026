import pandas as pd
df_vendas=pd.read_excel('vendas_roupas.xlsx')
print(df_vendas.head())


#Total de unidades vendidas 
print(f'\n O total de unidades vendidas foi R${df_vendas['Faturamento Total (R$)'].sum()}')

#Preço médio por unidade 
print(f'\n O preço médio por unidades vendidas foi R${df_vendas['Preco por Unidade (R$)'].mean()}')

#Maior Faturamento Total 
print(f'O maior faturamento Total')
maximo = df_vendas['Faturamento Total (R$)'].max()
print(df_vendas[df_vendas['Faturamento Total (R$)'] == maximo][['Faturamento Total (R$)']])
      
#Menor faturamento Total 
print(f'O menor faturamento Total')
menor = df_vendas['Faturamento Total (R$)'].min()
print(df_vendas[df_vendas['Faturamento Total (R$)'] == menor][['Faturamento Total (R$)']])


#Produto com menor faturamento 
print(f'O Produto com o menor faturamento Total')
print(df_vendas[df_vendas['Faturamento Total (R$)'] == menor][['Produto','Faturamento Total (R$)']])


#Produto com maior faturamento 
print(f'O Produto com o maior faturamento Total')
print(df_vendas[df_vendas['Faturamento Total (R$)'] == maximo][['Produto', 'Faturamento Total (R$)']])


#Produtos com satisfação baixo 
print(f'\nOs produtos com satisfação Baixo são')
produtos_baixos = df_vendas[df_vendas['Satisfacao'] == 'BAIXO'][['Produto', 'Satisfacao']]
print(produtos_baixos)

#Produtos com satisfação Alto 
print(f'\nOs produtos com satisfação Alto são')
produtos_altos = df_vendas[df_vendas['Satisfacao'] == 'ALTO'][['Produto', 'Satisfacao']]
print(produtos_altos)



import pandas as pd 

vendas= pd.Series([32,45,28,50,38,42])
cancelamentos = pd.Series([3,5,2,8,4,6])

#Terceiro registro de vendas 
print (f'A terceira venda é: {vendas [2]}')

#Segundo, Quarto e Sexto 
print(f'A segunda, quarta e sexta venda são {vendas[[1,3,5]]} ')

#Mais de 40 vendas 
print (f'O registro com mais de 40 vendas é {vendas[vendas>40]}')

#Total de vendas 
totalvendas=sum(vendas)
totalcancelamentos=sum(cancelamentos)
print (f'O total de vendas foi de {[totalvendas-totalcancelamentos]} ')
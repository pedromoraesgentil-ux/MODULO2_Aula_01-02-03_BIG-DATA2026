import pandas as pd 


#series

quantidades = pd.Series ([
    10, 5, 8, 12, 7, 15, 20, 6, 9, 11,
    4, 13, 18, 10, 5, 16, 8, 14, 7, 12,
    9, 6, 11, 15, 4, 18, 10, 7, 13, 5,
    16, 8, 12, 20, 6, 14, 9, 11, 17, 5
])

precos = pd.Series([
    25.50, 40.00, 15.90, 32.00, 18.50, 45.00, 60.00, 22.90, 35.00, 28.50,
    12.00, 50.00, 75.00, 30.00, 19.90, 55.00, 24.50, 42.00, 16.00, 38.50,
    29.90, 21.50, 34.00, 48.00, 14.90, 65.00, 27.50, 18.00, 44.90, 23.50,
    52.00, 31.50, 39.90, 70.00, 26.00, 47.50, 33.00, 20.90, 58.00, 17.50
])

#Acessar um elemento pelo índice
print (f'Índice 05: {quantidades [5]}')

#Acessar varios elementos pelo índice 
print (f'Índice 05: {quantidades [[5,10,15]]}')

#Filtrando valores acima de 40 
print (precos[precos >40 ])

#Operações matematicas 
print ('\n Dobrando a Série')
print (quantidades*2)

#Operações entre Séries 
total = quantidades*precos
print(f'Calculando o total {total}')


       




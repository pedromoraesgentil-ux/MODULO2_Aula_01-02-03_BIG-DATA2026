

print('\nMedidas de Tendência Central')
print(50 * '-')
print(f'Média: {media}')
print(f'Mediana: {mediana}')


#calculando quartis 

q1= np.quantile(array_vendas,.25)
q2= np.quantile(array_vendas,.50)
q3= np.quantile(array_vendas,.75)
q4= np.quantile(array_vendas,.100)

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


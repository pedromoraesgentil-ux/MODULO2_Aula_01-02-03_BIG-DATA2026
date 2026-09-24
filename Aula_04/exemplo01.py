#pip install pandas sqlalchemy pymysql
import pandas as pd
from sqlalchemy import create_engine


#Variaveis de conexão

host = 'localhost'
user = 'root'
password = ''
database = 'bd_aula04'

#Criando a coneção 
engine = create_engine ( 
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
)

#Consultas 
query1 = 'SELECT * FROM cadastro_produtos;'
query2 = 'SELECT * FROM cadastro_produtos WHERE Marca = "Hashtag" AND `Preço Unitario` >20'


df_produtos= pd.read_sql(query2, engine)
print(df_produtos)

#Produtos do Hashtag com preço maior do que 20

print({query2})









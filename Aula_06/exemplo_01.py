# pip install pandas sqlalchemy pymysql
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


# Variáveis de conexão
DB_host = 'localhost'
DB_user = 'root'
DB_password = ''
DB_database = 'bd_aula05_pedidos'

#Carrega variáveis de ambiente 
load_dotenv()

def conecta_banco():
    host = os.getenv ('DB_host')
    user = os.getenv ('DB_user')
    password = os.getenv ('DB_password')
    database = os.getenv ('DB_database')
    
    #url de conexão com banco 
    engine = create_engine(
    f'mysql+pympysql://{user}:{password}@{host}/{database}'
    )
    
    return engine
    
engine = conecta_banco()

try:
    df_usuario= pd.read_sql('tb_usuarios', engine)
    df_livros= pd.read_sql('tb_livros', engine)
    df_alugados=pd.read_sql('tb_alugados',engine)
    df_itens=pd.read_sql('itens_itens',engine)
    print(df_itens)
    
except Exception as e : 
    print (f'Erro ao conectar aos dados {e}')

#Relacionando os dadaframes com merge
try:
    
except Exception as e:
    print(f'Erro ao relacionar os dataframes {e}')









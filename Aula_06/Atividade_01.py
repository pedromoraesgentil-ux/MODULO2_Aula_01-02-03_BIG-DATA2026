# pip install pandas sqlalchemy pymysql
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os


# Variáveis de conexão
DB_host = 'localhost'
DB_user = 'root'
DB_password = ''
DB_database = 'bd_aula05'

#Carrega variáveis de ambiente 
load_dotenv()

def conecta_banco():
    host = os.getenv ('DB_host')
    user = os.getenv ('DB_user')
    password = os.getenv ('DB_password')
    database = os.getenv ('DB_database')
    
    #url de conexão com banco corrigida para pymysql
    engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}/{database}'
    )
    
    return engine
    
engine = conecta_banco()

try:
    # Alterado para read_sql_table para funcionar com o nome da tabela
    df_usuario= pd.read_sql_table('tb_usuarios', engine)
    df_livros= pd.read_sql_table('tb_livros', engine)
    df_alugados=pd.read_sql_table('tb_alugados', engine)
    df_itens=pd.read_sql_table('tb_itens_alugados', engine)
    print(df_itens)
    
except Exception as e : 
    print (f'Erro ao conectar aos dados {e}')

#Relacionando os dadaframes com merge
try:
    df_mergel1 = pd.merge(
        df_livros, df_itens, on='id_livro'
    )
    # Ajustado: parêntese fechado corretamente na mesma estrutura
    df_mergel2 = pd.merge(df_mergel1, df_alugados, on='id_aluguel')
    
    df_dados = pd.merge(
        df_mergel2, df_usuario
    )
    
    # Movido para dentro do try para imprimir apenas se os merges funcionarem
    print("\n--- DataFrame Final Consolidado ---")
    print(df_dados)

except Exception as e:
    print(f'Erro ao relacionar os dataframes {e}')

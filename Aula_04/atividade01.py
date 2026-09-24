# pip install pandas sqlalchemy pymysql
import pandas as pd
from sqlalchemy import create_engine

# Variáveis de conexão
host = 'localhost'
user = 'root'
password = ''
database = 'bd_aula04'

# Criando a conexão 
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# Consultas (Corrigido: fechamento de aspas na query2)
query1 = 'SELECT * FROM materiais_construcao;'
query2 = 'SELECT produto, preco FROM materiais_construcao;'
query3 = 'SELECT * FROM materiais_construcao WHERE categoria = "cimento";' 
query4 = 'SELECT * FROM materiais_construcao WHERE `preco` > 200 ORDER BY `preco`;'

# Executando as consultas separadamente (Corrigido: pd.read_sql aceita uma query por vez)
df_todos_produtos = pd.read_sql(query1, engine)
df_apenas_precos  = pd.read_sql(query2, engine)
df_cimentos       = pd.read_sql(query3, engine)
df_caros          = pd.read_sql(query4, engine)

# Exibindo os resultados dos DataFrames
print("--- Todos os Produtos ---")
print(df_todos_produtos)

print("\n--- Apenas Produto e Preço ---")
print(df_apenas_precos)

print("\n--- Apenas Cimentos ---")
print(df_cimentos)

print("\n--- Produtos Maiores que 200 (Ordenados) ---")
print(df_caros)

# Exibindo os textos das queries (Corrigido: removido o {} para evitar criar Sets)
print("\n--- Textos das Consultas SQL ---")
print(query1)
print(query2)
print(query3)
print(query4)


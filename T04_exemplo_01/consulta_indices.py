import sqlite3
import os

# Conectando ao banco de dados (será criado se não existir)
diretorio_atual = os.path.dirname(__file__)
caminho_baco_dados = os.path.join(diretorio_atual,'exemplo_indice.db')
conexao = sqlite3.connect(caminho_baco_dados)
cursor = conexao.cursor()

# Consulta para listar índices
cursor.execute('''
    SELECT name, tbl_name, sql
    FROM sqlite_master
    WHERE type = 'index'
''')

indices = cursor.fetchall()
print(f'{indices}\n')

cursor.execute('SELECT * FROM sqlite_master')
tabela_master = cursor.fetchall()


for indice in indices:
    print(f"Índice: {indice[0]} | Tabela: {indice[1]} | SQL: {indice[2]}")

print(tabela_master)
# Fechando a conexão
conexao.close()
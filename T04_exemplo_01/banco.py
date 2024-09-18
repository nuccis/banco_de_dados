import sqlite3
import os

# Conectando ao banco de dados (será criado se não existir)
diretorio_atual = os.path.dirname(__file__)
caminho_baco_dados = os.path.join(diretorio_atual,'exemplo_indice.db')
conexao = sqlite3.connect(caminho_baco_dados)
cursor = conexao.cursor()

# Criando a tabela de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Criando a tabela de vendas
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    valor REAL,
    data TEXT,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id)
)
''')

# Salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()
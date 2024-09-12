import sqlite3
import os

#Criando e conectando ao banco de dados
diretorio_atual = os.path.dirname(__file__)
caminho_banco_dados = os.path.join(diretorio_atual, 'vendas.db')
conexao = sqlite3.connect(caminho_banco_dados)
cursor = conexao.cursor()

# Criando a tabela de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

# Criando a tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco DECIMAL NOT NULL
)
''')

# Criando a tabela de vendas
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_total DECIMAL NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id),
    FOREIGN KEY(produto_id) REFERENCES produtos(id)
)
''')

# Inserindo dados na tabela clientes
clientes = [
    ('João',),
    ('Maria',),
    ('Carlos',)
]
cursor.executemany('INSERT INTO clientes (nome) VALUES (?)', clientes)

# Inserindo dados na tabela produtos
produtos = [
    ('Smartphone', 2000),
    ('Notebook', 3500),
    ('Geladeira', 3000)
]
cursor.executemany('INSERT INTO produtos (nome, preco) VALUES (?, ?)', produtos)

# Salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()

print("Banco de dados de vendas criado com sucesso!")

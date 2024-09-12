import sqlite3
import os

#Criando e conectando ao banco de dados
diretorio_atual = os.path.dirname(__file__)
caminho_banco_dados = os.path.join(diretorio_atual, 'estoque.db')
conexao = sqlite3.connect(caminho_banco_dados)
cursor = conexao.cursor()

# Criando a tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco DECIMAL NOT NULL,
    estoque INTEGER NOT NULL
)
''')

# Criando a tabela de compras
cursor.execute('''
CREATE TABLE IF NOT EXISTS compras (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_total DECIMAL NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY(produto_id) REFERENCES produtos(id)
)
''')

# Inserindo dados na tabela produtos
produtos = [
    ('Smartphone', 2000, 10),
    ('Notebook', 3500, 5),
    ('Geladeira', 3000, 2),
    ('TV', 2500, 4)
]
cursor.executemany('INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)', produtos)

# Salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()

print("Banco de dados de estoque criado com sucesso!")

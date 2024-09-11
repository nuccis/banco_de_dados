import sqlite3
import os

#Criando e conectando ao banco de dados
diretorio_atual = os.path.dirname(__file__)
caminho_banco_dados = os.path.join(diretorio_atual, 'loja.db')
conexao = sqlite3.connect(caminho_banco_dados)
cursor = conexao.cursor()

# Criando a tabela de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cidade TEXT NOT NULL
)
''')

# Criando a tabela de vendedores
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
''')

# Criando a tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    preco DECIMAL NOT NULL
)
''')

# Criando a tabela de vendas
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    vendedor_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_total DECIMAL NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id),
    FOREIGN KEY(vendedor_id) REFERENCES vendedores(id),
    FOREIGN KEY(produto_id) REFERENCES produtos(id)
)
''')

# Inserindo dados na tabela clientes
clientes = [
    ('João Silva', 'São Paulo'),
    ('Maria Oliveira', 'Rio de Janeiro'),
    ('Carlos Sousa', 'Salvador'),
    ('Ana Costa', 'Belo Horizonte'),
    ('Paulo Almeida', 'São Paulo')
]
cursor.executemany('INSERT INTO clientes (nome, cidade) VALUES (?, ?)', clientes)

# Inserindo dados na tabela vendedores
vendedores = [
    ('Roberto Santos',),
    ('Fernanda Lima',),
    ('Juliana Moreira',)
]
cursor.executemany('INSERT INTO vendedores (nome) VALUES (?)', vendedores)

# Inserindo dados na tabela produtos
produtos = [
    ('Smartphone', 'Eletrônicos', 2000),
    ('Geladeira', 'Eletrodomésticos', 3000),
    ('Notebook', 'Eletrônicos', 3500),
    ('TV', 'Eletrônicos', 2500),
    ('Fogão', 'Eletrodomésticos', 1800)
]
cursor.executemany('INSERT INTO produtos (nome, categoria, preco) VALUES (?, ?, ?)', produtos)

# Inserindo dados na tabela vendas
vendas = [
    (1, 1, 1, 2, 4000, '2024-08-01'),  # João comprou 2 Smartphones
    (2, 2, 2, 1, 3000, '2024-08-05'),  # Maria comprou 1 Geladeira
    (3, 1, 3, 1, 3500, '2024-08-10'),  # Carlos comprou 1 Notebook
    (4, 3, 4, 3, 7500, '2024-08-15'),  # Ana comprou 3 TVs
    (5, 1, 5, 1, 1800, '2024-08-20')   # Paulo comprou 1 Fogão
]
cursor.executemany('INSERT INTO vendas (cliente_id, vendedor_id, produto_id, quantidade, valor_total, data) VALUES (?, ?, ?, ?, ?, ?)', vendas)

# Salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso!")

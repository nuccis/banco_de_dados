import sqlite3
import os

#Criando e conectando ao banco de dados
diretorio_atual = os.path.dirname(__file__)
caminho_banco_dados = os.path.join(diretorio_atual, 'loja_ficticia.db')
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

# Criando a tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    preco REAL NOT NULL
)
''')

# Criando a tabela de vendas
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    valor_total REAL NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY(cliente_id) REFERENCES clientes(id),
    FOREIGN KEY(produto_id) REFERENCES produtos(id)
)
''')

# Inserindo dados na tabela de clientes
clientes = [
    ('João Silva', 'São Paulo'),
    ('Maria Souza', 'Rio de Janeiro'),
    ('Pedro Oliveira', 'Belo Horizonte'),
    ('Ana Lima', 'Curitiba'),
    ('Carlos Pereira', 'Porto Alegre')
]
cursor.executemany('INSERT INTO clientes (nome, cidade) VALUES (?, ?)', clientes)

# Inserindo dados na tabela de produtos
produtos = [
    ('Notebook', 'Eletrônicos', 2500.00),
    ('Smartphone', 'Eletrônicos', 1200.00),
    ('Geladeira', 'Eletrodomésticos', 1800.00),
    ('Televisão', 'Eletrônicos', 2200.00),
    ('Microondas', 'Eletrodomésticos', 600.00)
]
cursor.executemany('INSERT INTO produtos (nome, categoria, preco) VALUES (?, ?, ?)', produtos)

# Inserindo dados na tabela de vendas
vendas = [
    (1, 1, 1, 2500.00, '2024-08-01'),
    (2, 2, 2, 1200.00, '2024-08-05'),
    (3, 1, 3, 1800.00, '2024-08-08'),
    (4, 3, 4, 2200.00, '2024-08-10'),
    (5, 4, 5, 600.00, '2024-08-12'),
    (1, 3, 1, 2500.00, '2024-08-15'),
    (2, 4, 2, 1200.00, '2024-08-20')
]
cursor.executemany('INSERT INTO vendas (cliente_id, produto_id, quantidade, valor_total, data) VALUES (?, ?, ?, ?, ?)', vendas)

# Salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()

print("Banco de dados 'loja_ficticia.db' criado e populado com sucesso!")
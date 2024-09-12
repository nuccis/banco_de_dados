import sqlite3
import os

#Criando e conectando ao banco de dados
diretorio_atual = os.path.dirname(__file__)
caminho_banco_dados = os.path.join(diretorio_atual, 'banco.db')
conexao = sqlite3.connect(caminho_banco_dados)
cursor = conexao.cursor()

# Criando a tabela de contas
cursor.execute('''
CREATE TABLE IF NOT EXISTS contas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    saldo DECIMAL NOT NULL
)
''')

# Criando a tabela de movimentacoes
cursor.execute('''
CREATE TABLE IF NOT EXISTS movimentacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conta_origem_id INTEGER NOT NULL,
    conta_destino_id INTEGER NOT NULL,
    valor DECIMAL NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY(conta_origem_id) REFERENCES contas(id),
    FOREIGN KEY(conta_destino_id) REFERENCES contas(id)
)
''')

# Inserindo dados na tabela contas
contas = [
    ('João', 5000),
    ('Maria', 3000),
    ('Carlos', 2000)
]
cursor.executemany('INSERT INTO contas (nome, saldo) VALUES (?, ?)', contas)

# Salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()

print("Banco de dados de contas bancárias criado com sucesso!")

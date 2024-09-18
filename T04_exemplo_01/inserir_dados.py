import sqlite3
from random import randint, uniform
from datetime import datetime, timedelta
import os

# Conectando ao banco de dados (será criado se não existir)
diretorio_atual = os.path.dirname(__file__)
caminho_baco_dados = os.path.join(diretorio_atual,'exemplo_indice.db')
conexao = sqlite3.connect(caminho_baco_dados)
cursor = conexao.cursor()

# Inserindo clientes fictícios
clientes = [
    ('João Silva', 'joao@dominio.com'),
    ('Maria Souza', 'maria@dominio.com'),
    ('Pedro Oliveira', 'pedro@dominio.com'),
    ('Ana Costa', 'ana@dominio.com'),
    ('Carlos Santos', 'carlos@dominio.com'),
]

cursor.executemany('''
    INSERT INTO clientes (nome, email) VALUES (?, ?)
''', clientes)

# Função para gerar datas aleatórias
def gerar_data_aleatoria():
    inicio = datetime(2023, 1, 1)
    fim = datetime(2024, 12, 31)
    return inicio + timedelta(days=randint(0, (fim - inicio).days))

# Inserindo vendas fictícias
for i in range(20):  # Vamos gerar 20 vendas aleatórias
    cliente_id = randint(1, len(clientes))
    valor = round(uniform(100.00, 5000.00), 2)  # Valor entre R$100 e R$5000
    data = gerar_data_aleatoria().strftime('%Y-%m-%d')
    
    cursor.execute('''
        INSERT INTO vendas (cliente_id, valor, data) VALUES (?, ?, ?)
    ''', (cliente_id, valor, data))

# Salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()

print("Dados inseridos com sucesso!")

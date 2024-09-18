import sqlite3
import os

# Conectando ao banco de dados (será criado se não existir)
diretorio_atual = os.path.dirname(__file__)
caminho_baco_dados = os.path.join(diretorio_atual,'exemplo_indice.db')
conexao = sqlite3.connect(caminho_baco_dados)
cursor = conexao.cursor()

# Criando um índice para a coluna 'email' na tabela 'clientes'
cursor.execute('''
CREATE INDEX idx_clientes_email ON clientes (email)
''')

# Criando um índice composto para as colunas 'cliente_id' e 'data' na tabela 'vendas'
cursor.execute('''
CREATE INDEX idx_vendas_cliente_data ON vendas (cliente_id, data)
''')

# Salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()
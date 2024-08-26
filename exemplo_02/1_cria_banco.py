import sqlite3
import os
    
#Obter diretório onde o script está localizado
diretorio_atual = os.path.dirname(__file__)

#Construir o caminho completo para o banco de dados na mesma pasta do script
caminho_banco_dados = os.path.join(diretorio_atual, 'projetos_eletricos.db')

#Conectando ao banco de dados (será criado se não existir)
conexao = sqlite3.connect(caminho_banco_dados)

#Criando um cursor para executar comandos SQL
cursor = conexao.cursor()

#Criando a tabela 'exemplo'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS exemplo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
''')

#Criando a tabela 'projetos', que se relaciona com a tabela 'exemplo'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS projetos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        pessoa_id INTEGER,
        FOREIGN KEY(pessoa_id) REFERENCES exemplo(id)
    )
''')

#salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()

print('Banco de dados e tabelas criadas com sucesso!')
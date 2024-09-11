import sqlite3
import os

#Obter o diretório atual
diretorio_atual = os.path.dirname(__file__)

#Criando o caminho inteiro do banco de dados
caminho_banco_dados = os.path.join(diretorio_atual, 'projetos.db')

#criando a conexão com o banco de dados, caso ele n exista é criado
conexao = sqlite3.connect(caminho_banco_dados)

#Criando um cursor para executar os comandos em SQL
cursor = conexao.cursor()

#Criando as tabelas funcionarios e projetos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS projetos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        pessoa_id INTEGER,
        FOREIGN KEY (pessoa_id) REFERENCES funcionarios(id)           
    )
''')

#Salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()
print('Banco de dados e tabelas criadas com sucesso!')
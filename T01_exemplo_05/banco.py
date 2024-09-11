import sqlite3
import os

#Obter o diretório atual
diretorio_atual = os.path.dirname(__file__)

#Criando o caminho inteiro do banco de dados
caminho_banco_dados = os.path.join(diretorio_atual, 'projetos.db')

#Criando a conexão com o banco de dados, caso ele não exista é criado
conexao = sqlite3.connect(caminho_banco_dados)

#Criando o cursor para executar os comandos em SQL
cursor = conexao.cursor()

#Criando as tabelas funcionarios e projetos
cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        contato TEXT           
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS projetos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        pessoa_id INTEGER,
        FOREIGN KEY(pessoa_id) REFERENCES funcionarios(id)
    )
''')

#Inserindo dados nas tabela funcionario
cursor.execute("INSERT INTO funcionarios (nome, contato) VALUES ('Leticia', 'leticia@outlook.com')")
cursor.execute("INSERT INTO funcionarios (nome, contato) VALUES ('Nucis', 'nucis@gmail.com')")
cursor.execute("INSERT INTO funcionarios (nome, contato) VALUES ('Fernando', 'fernando@hotmail.com')")
cursor.execute("INSERT INTO funcionarios (nome, contato) VALUES ('Vitor', 'vitor@outlook.com')")
cursor.execute("INSERT INTO funcionarios (nome, contato) VALUES ('Alandra', 'alandra@gmail.com')")

#Pegando os ids
cursor.execute("SELECT id FROM funcionarios WHERE nome = 'Nucis'")
nucis_id = cursor.fetchone()[0]
cursor.execute("SELECT id FROM funcionarios WHERE nome = 'Fernando'")
fernando_id = cursor.fetchone()[0]
cursor.execute("SELECT id FROM funcionarios WHERE nome = 'Vitor'")
vitor_id = cursor.fetchone()[0]
cursor.execute("SELECT id FROM funcionarios WHERE nome = 'Alandra'")
alandra_id = cursor.fetchone()[0]

#Inserindo dados na tabela projetos
cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES ('Projeto 1', 'Cozinha', ?)", (nucis_id,))
cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES ('Projeto 2', 'Apartamento', ?)", (nucis_id,))
cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES ('Projeto A', 'Sala', ?)", (fernando_id,))
cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES ('Projeto B', 'Quarto', ?)", (fernando_id,))
cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES ('Projeto C', 'Banheiro', ?)", (fernando_id,))
cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES ('Projeto 1', 'Salão', ?)", (vitor_id,))
cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES ('Projeto A', 'Sala comercial', ?)", (alandra_id,))
cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES ('Projeto B', 'Restaurante', ?)", (alandra_id,))

#Salvando e fechando a conexão
conexao.commit()
conexao.close()

print('Operação realizada com sucesso!')
import sqlite3
import os

#Criando o caminho para acessar o banco de dados
diretorio = os.path.dirname(__file__)
caminho_banco_dados = os.path.join(diretorio, 'projetos.db')

#Criando uma conexão com o banco de dados
conexao = sqlite3.connect(caminho_banco_dados)

#Criando um cursor para executar os camandos em SQL
cursor = conexao.cursor()

#Inserindo dados nas tabela funcionario
cursor.execute("INSERT INTO funcionarios (nome) VALUES ('Leticia')")
cursor.execute("INSERT INTO funcionarios (nome) VALUES ('Nucis')")
cursor.execute("INSERT INTO funcionarios (nome) VALUES ('Fernando')")
cursor.execute("INSERT INTO funcionarios (nome) VALUES ('Vitor')")
cursor.execute("INSERT INTO funcionarios (nome) VALUES ('Alandra')")

#Pegando o id de Nucis e Fernando
cursor.execute("SELECT id FROM funcionarios WHERE nome = 'Nucis'")
nucis_id = cursor.fetchone()[0]
cursor.execute("SELECT id FROM funcionarios WHERE nome = 'Fernando'")
fernando_id = cursor.fetchone()[0]

#Inserindo dados na tabela projetos
cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES ('Projeto 1', 'Cozinha', ?)", (nucis_id,))
cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES ('Projeto 2', 'Apartamento', ?)", (nucis_id,))
cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES ('Projeto A', 'sala', ?)", (fernando_id,))

#Salvando e fechando a conexão
conexao.commit()
conexao.close()

print('Dados inseridos com sucesso!')
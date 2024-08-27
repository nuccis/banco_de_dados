import sqlite3
import os

#Criando o caminho para o banco de dados
diretorio = os.path.dirname(__file__)
caminho_banco_dados = os.path.join(diretorio, 'projetos.db')

#Criando a conexão e o cursor
conexao = sqlite3.connect(caminho_banco_dados)
cursor = conexao.cursor()

#Pegando o id de Nucis
cursor.execute("SELECT id FROM funcionarios WHERE nome = 'Nucis'")
nucis_id = cursor.fetchone()[0]

#Consultando os projetos de Nucis ordenados pelo nome
cursor.execute("SELECT nome, descricao FROM projetos WHERE pessoa_id = ? ORDER BY nome", (nucis_id,))
projetos_ordenados = cursor.fetchall()

for projeto in projetos_ordenados:
    print(f'Projeto: {projeto[0]}, Descrição: {projeto[1]}')

#Fechando a conexão
conexao.close()
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

#Consultando quantos projetos a Nucis tem
cursor.execute("SELECT COUNT(*) FROM projetos WHERE pessoa_id = ?", (nucis_id,))
quantidade_projetos = cursor.fetchone()[0]

print(f'Nucis tem {quantidade_projetos} projeto(s) cadastrados.')

#Fechando a conexão
conexao.close()
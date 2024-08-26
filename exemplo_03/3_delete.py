import sqlite3
import os

#Criando o caminho para o banco de dados
diretorio = os.path.dirname(__file__)
caminho_banco_dados = os.path.join(diretorio, 'projetos.db')

#Criando a conexão eo cursor
conexao = sqlite3.connect(caminho_banco_dados)
cursor = conexao.cursor()

#Identificando o id de nucis
cursor.execute("SELECT id FROM funcionarios WHERE nome = 'Nucis'")
nucis_id = cursor.fetchone()[0]

#Excluindo o projeto chamado 'Projeto 1' que pertence a Nucis
cursor.execute("DELETE FROM projetos WHERE nome = 'Projeto 1' AND pessoa_id = ?", (nucis_id,))

#Salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()

print('Projeto excluído com sucesso!')
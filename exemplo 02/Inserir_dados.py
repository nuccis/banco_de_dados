import sqlite3
import os

#Obter diretório onde o script está localizado
diretorio_atual = os.path.dirname(__file__)

#Construir o caminho completo para o banco de dados na mesma pasta do script
caminho_banco_dados = os.path.join(diretorio_atual, 'projetos_eletricos.db')

#Criar uma conexão e o cursor
conexao = sqlite3.connect(caminho_banco_dados)
cursor = conexao.cursor()

#Inserindo dados na tabela exemplo
#cursor.execute("INSERT INTO exemplo (nome) VALUES ('Leticia')")
#cursor.execute("INSERT INTO exemplo (nome) VALUES ('Nucis')")

#Pegando o id da pessoa 'Nucis'
cursor.execute("SELECT id FROM exemplo WHERE nome = 'Nucis'")
nucis_id = cursor.fetchone()[0]
#print(nucis_id)

#Inserindo projetos relacionados à pessoa Nucis
cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES ('Projeto A', 'Cozinha ampla', ?)", (nucis_id,))
cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES ('ProjetoB', 'Quarto suíte', ?)", (nucis_id,))

#Salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()
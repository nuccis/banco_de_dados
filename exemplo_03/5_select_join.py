import sqlite3
import os

#Criando o caminho para o banco de dados
diretorio = os.path.dirname(__file__)
caminho_banco_dados = os.path.join(diretorio, 'projetos.db')

#Criando a conexão e o cursor
conexao = sqlite3.connect(caminho_banco_dados)
cursor = conexao.cursor()

#Consultando todos os projetos e os nomes das pessoas responsáveis
cursor.execute('''
    SELECT projetos.nome, projetos.descricao, funcionarios.nome
    FROM projetos
    JOIN funcionarios ON projetos.pessoa_id = funcionarios.id
''')

#Obtendo e exibindo os resultados
projetos = cursor.fetchall()
print(projetos)

for projeto in projetos:
    print(f'Projeto: {projeto[0]}, Descrição: {projeto[1]}, Responsável: {projeto[2]}')

#Fechando a conexão
conexao.close()
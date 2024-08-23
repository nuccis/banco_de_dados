import sqlite3
import os

#Obter o diretório onde o script está localizado
diretorio_atual = os.path.dirname(__file__)

#Criando o endereço completo
caminho_banco_dados = os.path.join(diretorio_atual, 'projetos_eletricos.db')

#Criando a conexao e o cursor
conexao = sqlite3.connect(caminho_banco_dados)
cursor = conexao.cursor()

#Realizando uma consulta para trazer projetos relacionados à pessoa Nucis
cursor.execute('''
SELECT projetos.nome, projetos.descricao
FROM projetos
JOIN exemplo ON projetos.pessoa_id = exemplo.id
WHERE exemplo.nome = 'Nucis'
''')

projetos_de_nucis = cursor.fetchall()
print(projetos_de_nucis)

for num, projeto in enumerate(projetos_de_nucis):
    print(f'\nProjeto nº {num+1}')
    print(f'Nome do projeto: {projeto[0]}')
    print(f'Descrição do Projeto: {projeto[1]}')

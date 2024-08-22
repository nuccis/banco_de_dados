import sqlite3
import os

#Obtendo o diretório atual
diretorio_atual = os.path.dirname(__file__)

#Construir o caminho completo para o banco de dados na mesma pasta do script
caminho_banco_dados = os.path.join(diretorio_atual, 'meu_banco.db')

#criando uma conexão ao banco de dados - caso o banco não exista será criado
conexao = sqlite3.connect(caminho_banco_dados)

#Criando um cursos para executar comandos SQL
cursor = conexao.cursor()

#Executando um comando SQL para criar uma tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS exemplo (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL    
    )
''')

#Executando um comando SQL para inserir dados
#cursor.execute("INSERT INTO exemplo (nome) VALUES ('Amanda')")

#Executando uma consulta para selecionar dados
cursor.execute("SELECT * FROM exemplo")
dados = cursor.fetchall() #pegando todos os registros
print(type(dados))

print(dados)

#Salvando as mudanças e fechando a conexão
conexao.commit() #Comando responsável por salvar permanetemente as alterações feitas no banco de dados
conexao.close() #Este comando fecha a conexão com o banco de dados
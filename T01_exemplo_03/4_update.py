import sqlite3
import os

#Criando o caminho do banco de dados
diretorio = os.path.dirname(__file__)
caminho_banco_dados = os.path.join(diretorio, 'projetos.db')

#Criando a conexão e o cursor
conexao = sqlite3.connect(caminho_banco_dados)
cursor = conexao.cursor()

#Buscando o id do Fernando
cursor.execute("SELECT id FROM funcionarios WHERE nome = 'Fernando'")
fernando_id = cursor.fetchone()[0]

#Atualizando a descrição do projeto A do fernando
nova_descricao = 'Banheiro'
cursor.execute("UPDATE projetos SET descricao = ? WHERE nome = 'Projeto A' AND pessoa_id = ?", (nova_descricao, fernando_id))

#Salvando as mudanças e fechando a conexão
conexao.commit()
conexao.close()

print('Descrição do projeto atualizada com sucesso!')
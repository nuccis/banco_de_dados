import sqlite3
import os

#Criando o caminho do banco de dados
diretorio = os.path.dirname(__file__)
caminho_banco_dados = os.path.join(diretorio, 'projetos.db')

#Funções
def criar_tabelas():
    #Criando a conexao e o cursor
    conexao = sqlite3.connect(caminho_banco_dados)
    cursor = conexao.cursor()

    #Tabela de pessoas (clientes/responsáveis)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            contato TEXT
        )
    ''')

    #Tabela de projetos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS projetos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXTO NOT NULL,
        descricao TEXT,
        pessoa_id INTEGER,
        FOREIGN KEY(pessoa_id) REFERENCES pessoas(id)           
        )
    ''')

    #Salvando e fechando a conexão
    conexao.commit()
    conexao.close()

def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    contato = input("Digite o contato da pessoa: ")

    conexao = sqlite3.connect(caminho_banco_dados)
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO pessoas (nome, contato) VALUES (?, ?)", (nome, contato))

    conexao.commit()
    conexao.close()

    print("Pessoa cadastrada com sucesso!")

def cadastrar_projeto():
    conexao = sqlite3.connect('projetos.db')
    cursor = conexao.cursor()

    #Selecionar as pessoas
    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()

    if pessoas:
        pass
    else:
        print("Nenhuma pessoa cadastrada")
    
    conexao.commit()
    conexao.close()

    print('Cadastramento realizado com sucesso!')
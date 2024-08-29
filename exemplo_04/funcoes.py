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
    conexao = sqlite3.connect(caminho_banco_dados)
    cursor = conexao.cursor()

    #Selecionar as pessoas
    cursor.execute("SELECT * FROM pessoas")
    pessoas = cursor.fetchall()

    if pessoas:
        print("Selecione uma pessoa para associar o projeto:")
        for pessoa in pessoas:
            print(f'{pessoa[0]} - {pessoa[1]}')
            
        pessoa_id = int(input("Digite o ID da pessoa: "))

        nome_projeto = input("Digite o nome do projeto: ")
        descricao_projeto = input("Digite a descrição do projeto: ")

        cursor.execute("INSERT INTO projetos (nome, descricao, pessoa_id) VALUES (?, ?, ?)", (nome_projeto, descricao_projeto, pessoa_id))

        print('Cadastramento realizado com sucesso!')
    else:
        print("Nenhuma pessoa cadastrada")
    
    conexao.commit()
    conexao.close()


def visualizar_pessoas_projetos():
    conexao = sqlite3.connect(caminho_banco_dados)
    cursor = conexao.cursor()

    cursor.execute('''
        SELECT pessoas.nome, pessoas.contato, projetos.nome, projetos.descricao
        FROM pessoas
        LEFT JOIN projetos ON pessoas.id = projetos.pessoa_id
    ''')
    #O LEFT JOIN retorna todos os registros da tabela à esquerda, mesmo que não haja correspondências na tabela à direita.
    resultados = cursor.fetchall()

    if resultados:
        for pessoa in resultados:
            print(f'Pessoa: {pessoa[0]} | Contato: {pessoa[1]} | Projeto: {pessoa[2]} | Descrição: {pessoa[3]}')
    else:
        print('Nenhum dado encontrado.')
    
    conexao.close()

def excluir_projeto():
    conexao = sqlite3.connect(caminho_banco_dados)
    cursor = conexao.cursor()

    #Listar os projetos para o usuário escolher
    cursor.execute("SELECT * FROM projetos")
    projetos = cursor.fetchall()

    print("Selecione o projeto que deseja excluir:")
    for projeto in projetos:
        print(f'{projeto[0]} - {projeto[1]}')
    
    projeto_id = int(input('Digite o ID do projeto: '))
    
    cursor.execute("DELETE FROM projetos WHERE id = ?", (projeto_id,))

    conexao.commit()
    conexao.close()

    print('Projeto excluído com sucesso!')

def atualizar_contato_pessoa():
    conexao = sqlite3.connect(caminho_banco_dados)
    cursor = conexao.cursor()

    #Listar as pessoas para o usuário escolher
    cursor.execute('SELECT * FROM pessoas')
    pessoas = cursor.fetchall()

    if pessoas:
        print('Selecione a pessoa cujo contato deseja atualizar:')
        for pessoa in pessoas:
            print(f'{pessoa[0]} - {pessoa[1]}')
        
        pessoa_id = int(input('Digite o ID da pessoa: '))
        novo_contato = input("Digite o novo contato: ")

        cursor.execute("UPDATE pessoas SET contato = ? WHERE id = ?", (novo_contato, pessoa_id))
    else:
        print('Nenum cadastro encontrado')
    
    conexao.commit()
    conexao.close()

def menu():
    while True:
        print('\nMenu:')
        print('1 - Cadastrar Pessoa')
        print('2 - Cadastrar Projeto')
        print('3 - Visualizar Pessoas e Projetos')
        print('4 - Atualizar Contato de Pessoa')
        print('5 - Excluir Projeto')
        print('0 - sair')

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            cadastrar_projeto()
        elif opcao == '3':
            visualizar_pessoas_projetos()
        elif opcao == '4':
            atualizar_contato_pessoa()
        elif opcao == '5':
            excluir_projeto()
        elif opcao == '0':
            print('Saindo do programa...')
            break
        else:
            print('Opção Inválida. Tente novamente.')
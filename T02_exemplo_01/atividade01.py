import sqlite3
import os

def simular_compra(itens_compra):
    try:
        #Criando e conectando ao banco de dados
        diretorio_atual = os.path.dirname(__file__)
        caminho_banco_dados = os.path.join(diretorio_atual, 'estoque.db')
        conexao = sqlite3.connect(caminho_banco_dados)
        cursor = conexao.cursor()

        #Iniciar uma transação
        cursor.execute('BEGIN')

        #Iterar sobre os itens que estão sendo comprados
        for produto_id, quantidade_comprada in itens_compra:
            #Verificar o estoque atual do produto
            cursor.execute('SELECT estoque FROM produtos WHERE id =?', (produto_id,))
            resultado = cursor.fetchone()
            print(resultado)
            if resultado is None:
                raise ValueError(f'Produto com ID {produto_id} não encontrado.')
    
    except Exception as e:
        print(f"Erro ao realizar a compra: {e}")
    
    finally:
        conexao.close()


itens_compra = [(1,3), #Produto ID 1, quantidade 3
                (2,2), #Produto ID 2, quantidade 2
                (3,1)] #Produto ID 3, quantidade 1

#main
simular_compra(itens_compra)
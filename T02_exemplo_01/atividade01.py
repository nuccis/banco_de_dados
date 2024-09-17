#Simular uma compra de vários itens em uma transação
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
            estoque_atual = resultado[0]

            if estoque_atual < quantidade_comprada:
                raise ValueError(f'Estoque insuficiente para o produto {produto_id}\n (Disponível: {estoque_atual}, Solicitado: {quantidade_comprada})')
            
            novo_estoque = estoque_atual - quantidade_comprada
            cursor.execute('UPDATE produtos SET estoque = ? WHERE id = ?', (novo_estoque, produto_id))
        
        #Se tudo estiver certo, confirmar a transação
        conexao.commit()
        print('Compra realizada com sucesso!')
    
    except Exception as e:
        conexao.rollback()
        print(f"Erro ao realizar a compra: {e}")
    
    finally:
        conexao.close()


itens_compra = [(1,1), #Produto ID 1, quantidade 3
                (2,2), #Produto ID 2, quantidade 2
                (3,1)] #Produto ID 3, quantidade 1

#main
simular_compra(itens_compra)
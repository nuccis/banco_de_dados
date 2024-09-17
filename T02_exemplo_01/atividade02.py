#Criar uma transação que mova dinheiro entre contas
import sqlite3
import os

def mover_dinheiro(id_pagador, id_recebedor, valor):
    try:
        #Criando a conexão com o banco de dados e o cursor
        diretorio_atual = os.path.dirname(__file__)
        caminho_banco_dados = os.path.join(diretorio_atual, 'banco.db')
        conexao = sqlite3.connect(caminho_banco_dados)
        cursor = conexao.cursor()

        #Iniciar uma transação
        conexao.execute('BEGIN')

        #Checando se é possível fazer a transação
        cursor.execute('SELECT saldo FROM contas WHERE id = ?', (id_pagador,))
        resultado = cursor.fetchone()
        if resultado is None:
            raise ValueError(f'Conta com id {id_pagador} não encontrada')
        saldo_pagador = resultado[0]

        cursor.execute('SELECT saldo FROM contas WHERE id = ?', (id_recebedor,))
        resultado = cursor.fetchone()
        if resultado is None:
            raise ValueError(f'Conta com id {id_recebedor} não encontrada')
        saldo_recebedor = resultado[0]

        if saldo_pagador < valor:
            raise ValueError(f'Saldo insuficiente. Saldo atual: R${saldo_pagador},00 - Valor a pagar R${valor},00')

        #Realizando a transação
        saldo_pagador -= valor
        saldo_recebedor += valor

        cursor.execute('UPDATE contas SET saldo = ? WHERE id = ?', (saldo_pagador, id_pagador))
        cursor.execute('UPDATE contas SET saldo = ? WHERE id = ?', (saldo_recebedor, id_recebedor))       

        #Confirmando a transação
        conexao.commit()
        print('Transação realizada com sucesso!') 
    except Exception as e:
        conexao.rollback()
        print(f'Erro ao realizar a transação: {e}')
    finally:
        conexao.close()

mover_dinheiro(1, 2, 300)
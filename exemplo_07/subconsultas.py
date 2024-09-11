import sqlite3
import os

#Criando e conectando ao banco de dados
diretorio_atual = os.path.dirname(__file__)
caminho_banco_dados = os.path.join(diretorio_atual, 'loja.db')
conexao = sqlite3.connect(caminho_banco_dados)
cursor = conexao.cursor()

#Ordenar os clientes pelo total de compras, do maior para o menor
print('\nOrdenar os clientes pelo total de compras, do maior para o menor')
cursor.execute('''--sql 
    SELECT clientes.nome, SUM(vendas.valor_total) AS total_compras
    FROM vendas
    JOIN clientes ON clientes.id = vendas.cliente_id
    GROUP BY clientes.nome     
    ORDER BY total_compras DESC          
--endsql''')
resultado = cursor.fetchall()
print(resultado) 

#Ordenar os clientes pelo total de compras, do maior para o menor e limitar em 3
print('\nOrdenar os clientes pelo total de compras, do maior para o menor e limitar em 3')
cursor.execute('''--sql 
    SELECT clientes.nome, SUM(vendas.valor_total) AS total_compras
    FROM vendas
    JOIN clientes ON clientes.id = vendas.cliente_id
    GROUP BY clientes.nome     
    ORDER BY total_compras DESC          
    LIMIT 3
--endsql''')
resultado = cursor.fetchall()
print(resultado) 

#Fechando conexão
conexao.close()
import sqlite3
import os

#Criando e conectando ao banco de dados
diretorio_atual = os.path.dirname(__file__)
caminho_banco_dados = os.path.join(diretorio_atual, 'loja_ficticia.db')
conexao = sqlite3.connect(caminho_banco_dados)
cursor = conexao.cursor()

#Contagem de vendas por produto
print('\nContagem de vendas por produto')
cursor.execute('''--sql 
    SELECT produto_id, COUNT(*) AS total_vendas
    FROM vendas
    GROUP BY produto_id               
--endsql''')
resultado = cursor.fetchall()
print(resultado)

#Quantidade de produto vendido por tipo de produto
print('\nQuantidade de produto vendido por tipo de produto')
cursor.execute('''--sql 
    SELECT produto_id, SUM(quantidade) AS total_produto_vendido
    FROM vendas
    GROUP BY produto_id
--endsql''')
resultado = cursor.fetchall()
print(resultado)

#Soma das vendas pro produto
print('\nSoma das vendas por produto')
cursor.execute('''--sql 
    SELECT produto_id, SUM(valor_total) AS valor_total_venda
    FROM vendas
    GROUP BY produto_id               
--endsql''')
resultado = cursor.fetchall()
print(resultado)

#Média de vendas por categoria
print('\nMédia de venda por categoria')
cursor.execute('''--sql  
    SELECT produtos.categoria, AVG(vendas.valor_total) AS media_vendas
    FROM vendas
    JOIN produtos ON vendas.produto_id = produtos.id
    GROUP BY produtos.categoria             
--endsql''')
resultado = cursor.fetchall()
print(resultado)

#Valor máximo e mínimo de Vendas por vendedor
print('\nValor máximo e mínimo de vendas por vendedor')
cursor.execute('''--sql 
    SELECT clientes.nome, MAX(vendas.valor_total) AS venda_maxima, MIN(vendas.valor_total) AS venda_minima
    FROM vendas
    JOIN clientes ON vendas.cliente_id = clientes.id
    GROUP BY clientes.nome               
--endsql''')
resultado = cursor.fetchall()
print(resultado)

#Filtrando produtos com mais de 1 venda
print('\nFiltrando produtos com mais de 1 venda')
cursor.execute('''--sql 
    SELECT produto_id, COUNT(*) AS vendas_totais
    FROM vendas
    GROUP BY produto_id
    HAVING vendas_totais > 1               
--endsql''')
resultado = cursor.fetchall()
print(resultado)

#Fechando conexão
conexao.close()
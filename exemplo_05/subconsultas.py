import sqlite3
import os

#Obter o diretório atual
diretorio_atual = os.path.dirname(__file__)

#Criando o caminho inteiro do banco de dados
caminho_banco_dados = os.path.join(diretorio_atual, 'projetos.db')

#Criando a conexão com o banco de dados, caso ele não exista é criado
conexao = sqlite3.connect(caminho_banco_dados)

#Criando o cursor para executar os comandos em SQL
cursor = conexao.cursor()

#Subconsulta escalar
print('\nSubconsulta escalar')
cursor.execute('''--sql
    SELECT *
    FROM projetos
    WHERE pessoa_id = (SELECT id FROM funcionarios WHERE nome = 'Nucis')
--endsql''')
resultado = cursor.fetchall()
print(resultado)

#Subconsulta de linhas (esse exemplo não faz sentido, pois sem a criação de uma nova tabela dava para resolver o problema... Mas é útil para mostrar que podemos criar uma nova tabela a partir da filtragem de outra)
print('\nSubconsulta com filtragem e criação de nova tabela')
cursor.execute('''--sql
    SELECT projetos.nome, projetos.descricao, subquery_pessoas.nome AS pessoa
    FROM projetos
    JOIN (SELECT id, nome FROM funcionarios) AS subquery_pessoas
    ON projetos.pessoa_id = subquery_pessoas.id
--endsql''')
resultado = cursor.fetchall()
print(resultado)

#Subconsulta dentro da seleção principal (faz uma iteração linha a linha)
#Para esse exemplo abaixo:
    #Consulta Principal: Para cada pessoa na tabela pessoas, a consulta principal retorna o nome dessa pessoa.
    #Subconsulta: Para cada funcionario, uma subconsulta é executada para contar quantos projetos têm o pessoa_id igual ao id da pessoa atual.
    #Resultado: O resultado final contém o nome de cada pessoa e o total de projetos que pertencem a ela.
# Essa consulta pode ser ineficiente em grandes bases de dados, porque a subconsulta é executada para cada linha da tabela funcionários.
#Uma alternativa mais eficiente é utilizar JOIN seguido de GROUP BY
print('\nSubconsulta dentro da seleção principal')
cursor.execute('''--sql 
    SELECT nome, (SELECT COUNT(*) FROM projetos WHERE projetos.pessoa_id = funcionarios.id) AS total_projetos
    FROM funcionarios               
--endsql''')
resultado = cursor.fetchall()
print(resultado)

#Alternativa ao exemplo acima
#Essa é uma melhor alternativa ao exemplo acima
print('\nSubconsulta com join e group by')
cursor.execute('''--sql 
    SELECT funcionarios.nome, COUNT(projetos.id) AS total_projetos
    FROM funcionarios
    LEFT JOIN projetos ON funcionarios.id = projetos.pessoa_id
    GROUP BY funcionarios.nome              
--endsql''')
resultado = cursor.fetchall()
print(resultado)

#Subconsulta com cálculo de métrica
print('\nSubconsulta com cálculo de métrica')
cursor.execute('''--sql
    SELECT funcionarios.nome, projetos_por_pessoa.total_projetos
    FROM funcionarios
    LEFT JOIN
        (SELECT pessoa_id, COUNT(*) AS total_projetos
        FROM projetos
        GROUP BY pessoa_id) AS projetos_por_pessoa
    ON funcionarios.id = projetos_por_pessoa.pessoa_id
--endsql''')
resultado = cursor.fetchall()
print(resultado)

#Fechando a conexão
conexao.close()
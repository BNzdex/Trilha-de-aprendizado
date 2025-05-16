import sqlite3

conexao = sqlite3.connect("comercialtech.db") # Cria ou abre um banco de dados
cursor = conexao.cursor() # O cursor executa os comandos SQL

id_cliente = int(input("Digite o ID do cliente a ser alterado: ")) # Solicita o Id do cliente que vai ser alterado

# solicita os novos registros do cliente
nome = input("Digite o novo nome para registro: ")
email = input("Digite o e-mail: ")
telefone = input("Agora digite o telefone: ")

cursor.execute("""UPDATE Cliente
SET nome = ?, email = ?, telefone = ?
WHERE Id_cliente = ?
""", (nome, email, telefone, id_cliente))

# cursor.execute("""INSERT INTO Cliente (nome, email, telefone)  VALUES
# ('Bernardo', 'bernardoaraujo@gmail.com', '27996283448'),
# ('Lorrany', 'lorranybarcelos@gmail.com', '27996783888'),
# ('Maria', 'mariablabla@gmail.com', '27991287148'), 
# ('Ivo', 'ivogabriellivio@hotmail.com', '27996265278'),
# ('Lolo', 'loloooooo@gmail.com', '27994723448');
# """)

cursor.execute("""SELECT * FROM Cliente""")
clientes = cursor.fetchall() # Armazena e retona o que está dentro de uma tupla


for y in clientes:
    print(f'ID: {y[0]}\nNome: {y[1]}\nE-mail: {y[2]}\nTelefone: {y[3]}')

conexao.close() # Encerra a conexão

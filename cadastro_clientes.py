import sqlite3

conexao = sqlite3.connect("comercialtech.db") # Cria ou abre um banco de dados
cursor = conexao.cursor() # O cursor executa os comandos SQL

nome = input('Digite seu nome: ')
email = input('Digite seu e-mail: ')
telefone = input('Agora informe seu telefone: ')

cursor.execute("""INSERT INTO Cliente (nome, email, telefone) 
VALUES (?, ?, ?)
""", (nome, email, telefone))

conexao.commit() # Salva as mudanças

cursor.execute("""SELECT * FROM Cliente""")
clientes = cursor.fetchall() # Armazena e retona o que está dentro de uma tupla


for y in clientes:
    print(f'ID: {y[0]}\nNome: {y[1]}\nE-mail: {y[2]}\nTelefone: {y[3]}')

conexao.close() # Encerra a conexão
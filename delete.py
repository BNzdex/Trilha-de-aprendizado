import sqlite3

conexao = sqlite3.connect("comercialtech.db")
cursor = conexao.cursor()

usuario = input("Digite o ID do usuario a ser deletado: ")

cursor.execute("""Delete FROM Cliente WHERE Id_cliente = ?""", (usuario))

conexao.commit()

cursor.execute("SELECT * FROM Cliente")
clientes = cursor.fetchall()

for i in clientes:
    print(f"ID: {i[0]}\nNome: {i[1]}\nE-Mail: {i[2]}\nTelefone: {i[3]}")

conexao.close()
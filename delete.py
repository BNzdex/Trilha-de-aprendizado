import sqlite3  # Importa o módulo para trabalhar com SQLite

conexao = sqlite3.connect("comercialtech.db")  # Conecta (ou cria) o banco de dados
cursor = conexao.cursor()  # Cria o cursor para executar comandos SQL

usuario = input("Digite o ID do usuario a ser deletado: ")  # Pede o ID do cliente

# Deleta o cliente com o ID informado 
cursor.execute("""DELETE FROM Cliente WHERE Id_cliente = ?""", (usuario,))

conexao.commit()  # Salva as alterações no banco

# Seleciona todos os clientes restantes
cursor.execute("SELECT * FROM Cliente")
clientes = cursor.fetchall()

# Exibe os dados dos clientes
for i in clientes:
    print(f"ID: {i[0]}\nNome: {i[1]}\nE-Mail: {i[2]}\nTelefone: {i[3]}")

conexao.close()  # Fecha a conexão com o banco

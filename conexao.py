import sqlite3

conexao = sqlite3.connect("comercialtech.db") # Cria ou abre um banco de dados
cursor = conexao.cursor() # O cursor executa os comandos SQL

cursor.execute("PRAGMA foreign_keys = ON") # Para ser usado apenas quando ouver chave estrageira

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS Cliente (
Id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
nome VARCHAR(100) NOT NULL,
cpf CHAR(11) NOT NULL,
endereço VARCHAR(100) NOT NULL,
telefone CHAR(11) NOT NULL
);
""")

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS Produtos (
Id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
nome_produto VARCHAR(100) NOT NULL,
quantidade INT NOT NULL,
preco INT NOT NULL
 );
""")


# conexao.commit() Salva as mudanças
# conexao.close()  Encerra a conexão

cursor.execute("INSERT INTO Cliente (nome) VALUES ('Bernardo')")
cursor.execute("SELECT * FROM Cliente")
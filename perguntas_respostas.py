import sqlite3
import random

# Conectando (ou criando) o banco de dados
conn = sqlite3.connect('perguntas.db')
cursor = conn.cursor()

# Criando a tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS perguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pergunta TEXT NOT NULL,
    op_a TEXT NOT NULL,
    op_b TEXT NOT NULL,
    op_c TEXT NOT NULL,
    correta TEXT NOT NULL CHECK(correta IN ('a','b','c'))
)
''')
conn.commit()

def cadastrar_pergunta():
    print("\n--- Cadastrar Nova Pergunta ---")
    pergunta = input("Digite o enuciado da pergunta: ")
    op_a = input("Digite a opção A: ")
    op_b = input("Digite a opção B: ")
    op_c = input("Digite a opção C: ")
    correta = input("Qual é a alternativa correta? (a, b ou c): ").lower()
    
    while correta not in ('a', 'b', 'c'):
        correta = input("Opção inválida. Digite apenas 'a', 'b' ou 'c': ").lower()

    cursor.execute('''
    INSERT INTO perguntas (pergunta, op_a, op_b, op_c, correta)
    VALUES (?, ?, ?, ?, ?)
    ''', (pergunta, op_a, op_b, op_c, correta))
    conn.commit()
    print("Pergunta cadastrada com sucesso!\n")

def jogar():
    print("\n--- Iniciando o Jogo ---")

    cursor.execute('SELECT * FROM perguntas')
    perguntas = cursor.fetchall()

    if not perguntas:
        print("Nenhuma pergunta cadastrada. Cadastre perguntas primeiro.\n")
        return

    random.shuffle(perguntas)
    acertos = 0

    for pergunta in perguntas:
        id, pergunta, op_a, op_b, op_c, correta = pergunta
        print(f"\nPergunta: {pergunta}")
        print(f"A) {op_a}")
        print(f"B) {op_b}")
        print(f"C) {op_c}")
        resposta = input("Sua resposta (a, b ou c): ").lower()

        while resposta not in ('a', 'b', 'c'):
            resposta = input("Resposta inválida. Digite apenas 'a', 'b' ou 'c': ").lower()

        if resposta == correta:
            print("Resposta correta!")
            acertos += 1
        else:
            print(f"Resposta errada! A correta era: {correta.upper()}")

    print(f"\nFim do jogo! Você acertou {acertos} de {len(perguntas)} perguntas.\n")

# Menu principal
def menu():
    while True:
        print("=== Menu Principal ===")
        print("1. Cadastrar nova pergunta")
        print("2. Jogar")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_pergunta()
        elif opcao == '2':
            jogar()
        elif opcao == '3':
            print("Saindo... Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Iniciar o programa
menu()

# Fechar a conexão com o banco de dados
cursor.close()
conn.close()

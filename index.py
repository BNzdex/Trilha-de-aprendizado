import sqlite3

conexao = sqlite3.connect("comercialtech.db")
cursor = conexao.cursor()

while True:
    print ('{:=^50}'.format(' Escolha uma das opções '))
    print("""
    1- Criar cadastro
    2- Atualizar cadastro
    3- Deletar cadastro
    4- Listar cadastro""")
    opcao = int(input("Digite o número do que deseja fazer: "))

    if opcao == 1:
        nome = input("Digite o nome para registro: ")
        email = input("Digite o e-mail: ")
        telefone = input("Agora digite o telefone: ")
        
        cursor.execute("""INSERT INTO Cliente(nome, email, telefone) VALUES
        (?, ?, ?)""", (nome, email, telefone))
        print ("Cliente cadastrado com sucesso!")
        
    elif opcao == 2:
        id_atualizar = int(input("Digite o ID do cliente que deseja atualizar: "))
        
        nome = input("Digite o novo nome para registro: ")
        email = input("Digite o e-mail: ")
        telefone = input("Agora digite o telefone: ")

        cursor.execute("""UPDATE Cliente 
        SET nome = ?, email = ?, telefone = ? WHERE Id_cliente = ?
        """, (nome, email, telefone, id_atualizar))
        print("Cliente atualizado com sucesso!")

    elif opcao == 3:
        id_deletar = int(input("Digite o ID do Cliente que deseja deletar"))
        cursor.execute("""DELETE FROM Cliente WHERE Id_cliente = ?""", id_deletar)
        print("Cliente deletado com sucesso!")

    elif opcao == 4:
        cursor.execute("SELECT * FROM Cliente")
        clientes = cursor.fetchall()

        for y in clientes:
            print(f'ID: {y[0]}\nNome: {y[1]}\nE-mail: {y[2]}\nTelefone: {y[3]}')

    else:
        print("Opção inválida")

    conexao.commit()
    break
conexao.close() 

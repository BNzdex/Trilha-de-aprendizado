print ('\n{:=^50}'.format(' Cadastro do Cliente '))

nome = input('\nDigite seu nome :')
email = input('Digite seu e-mail :')
telefone = int(input('Digite seu telefone :'))

print ('\n{:=^50}'.format(' Cadastro do Produto '))

nome_produto = input('\nDigite o nome do produto :')
preco = float(input('Informe o preço do produto : '))
quantidade = int(input('Informe a quantidade de produtos no estoque : '))

print(f'\nO nome do cliente é {nome}, seu e-mail é {email} e seu telefone é {telefone}')
print(f'O produto é {nome_produto}, o preço é {preco} e a quantidade de produtos no estoque é {quantidade}\n')






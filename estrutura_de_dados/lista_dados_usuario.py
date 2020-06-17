#ler dados do usuário (nome, sobrenome, idade) 
#adicionar em uma lista 
#e imprimir seus elementos na tela

nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = input('Digite sua idade: ')

usuarios = []
usuarios.append(nome)
usuarios.append(sobrenome)
usuarios.append(idade)

print('Dados do usuário: {}'.format(usuarios))

#Dicionario
dados_pessoais = {'nome': nome, 'sobrenome': sobrenome, 'idade': idade }

print(dados_pessoais)
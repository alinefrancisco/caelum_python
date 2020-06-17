#utilizar um dict que leia dados de entrada do usuário. 
#O usuário deve entrar com os dados de uma pessoa como nome, 
#idade e cidade onde mora (fique livre para acrescentar outros). 
#e imprimir os dados como o exemplo abaixo:
#ex: nome: João
#    idade: 20
#    cidade: São Paulo

resposta = input("Deseja adicionar uma pessoa a lista ? [S/N] : ")

lista = []

while (resposta.upper() == 'S'):
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    cidade = input('Digite a cidade: ')
    
    pessoas = {'nome': nome, 'idade': idade, 'cidade': cidade}
    
    lista.append(pessoas)
    
    resposta = input("Deseja adicionar + uma pessoa a lista ? [S/N] : ")
    
for usuario in lista:
    print('nome: {} \n idade: {} \n cidade: {}'.format(usuario['nome'], usuario['idade'], usuario['cidade']))
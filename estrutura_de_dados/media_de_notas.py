#ler 4 notas, mostrar as notas e a média na tela.

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a segunda nota: '))
nota3 = int(input('Digite a terceira nota: '))
nota4 = int(input('Digite a quarta nota: '))

lista_notas = []
lista_notas.append(nota1)
lista_notas.append(nota2)
lista_notas.append(nota3)
lista_notas.append(nota4)

soma_das_notas = sum(lista_notas)
#qtde_de_notas = len(lista_notas)
media_das_notas = soma_das_notas / 4
print('Notas: {}'.format(lista_notas))
print('Média das notas: {} '.format(media_das_notas))


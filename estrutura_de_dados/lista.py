lista=[12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]

#imprimir o maior elemento
print('Maior elemento da lista: {}'.format(max(lista, key=int)))

#imprimir o menor elemento
print('Menor elemento da lista: {}'.format(min(lista, key=int)))

#imprimir os números pares
numeros_pares = []
for par in lista:
    if par % 2 == 0:
       numeros_pares.append(par)
       
print('Lista de números pares: {} '.format(numeros_pares))

#imprimir o número de ocorrências do primeiro elemento da lista
print('Lista de ocorrências: {} '.format(lista.count(lista[0])))

#imprimir a média dos elementos
soma_dos_elementos = sum(lista)
qtde_dos_elementos = len(lista)
media_dos_elementos = soma_dos_elementos / qtde_dos_elementos
print('Média dos elementos: {} '.format(media_dos_elementos))

#imprimir a soma dos elementos de valor negativo
soma_dos_negativos = sum(filter(lambda n: n < 0, lista))
print('Soma dos elementos negativos: {}'.format(soma_dos_negativos))
from random import randint

lista = list()

def sorteia(lista):
    for c in range(0,5):
        lista.append(randint(0,10))
    print(lista)

def somapar(lista):
    soma = 0
    for c in range(0,5):
        if lista[c] % 2 == 0:
            soma += lista[c]
    print(f'A soma dos números pares é {soma}')

sorteia(lista)
somapar(lista)
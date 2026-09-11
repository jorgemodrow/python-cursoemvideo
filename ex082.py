lista = []
par = []
impar = []
continuar = 'S'

while continuar == 'S':
    lista.append(int(input('Digite um valor: ')))

    while True:
        continuar = input('Deseja continuar? [S/N] ').upper()
        if continuar in 'SN':
            break

for numero in lista:
    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print(f'A lista completa é {lista}')
print(f'Os pares digitados foram {par}')
print(f'Os ímpares digitados foram {impar}')
lista = []
continuar = 'S'
while continuar == 'S':
    lista.append(int(input('Digite um valor: ')))

    while True:
        continuar = input('Deseja continuar? [S/N] ').upper()
        if continuar in 'SN':
            break

print(f'\nForam digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente: {lista}')

if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
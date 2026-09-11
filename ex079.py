lista = []
continuar = 'S'

while continuar == 'S':
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar')

    while True:
        continuar = input('Deseja continuar? [S/N] ').upper()
        if continuar in 'SN':
            break

    if continuar == 'N':
        break

lista.sort()
print(f'Você digitou os valores {lista}')
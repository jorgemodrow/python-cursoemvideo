soma_pares = soma_terceira_coluna = 0
matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-'*40)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
        if coluna == 2:
            soma_terceira_coluna += matriz[linha][coluna]

        if linha == 1:
            if coluna == 0:
                maior_segunda_linha = matriz[linha][coluna]
            else:
                if matriz[linha][coluna] > maior_segunda_linha:
                    maior_segunda_linha = matriz[linha][coluna]
    print()

print('-'*40)
print(f'\nSoma dos números pares: {soma_pares}')
print(f'Soma dos valores da 3ª coluna: {soma_terceira_coluna}')
print(f'Maior valor da 2ª linha: {maior_segunda_linha}')
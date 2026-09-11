tupla = (
    int(input('Digite o valor 1/4: ')),
    int(input('Digite o valor 2/4: ')),
    int(input('Digite o valor 3/4: ')),
    int(input('Digite o valor 4/4: '))
)

print(f'Você digitou os valores: {tupla}')

if tupla.count(9) == 0:
    print('O valor 9 não apareceu nenhuma vez')
else:
    print(f'O valor 9 apareceu {tupla.count(9)} vezes')

if 3 not in tupla:
    print('O valor 3 não apareceu nenhuma vez')
else:
    print(f'Posição que apareceu o primeiro valor 3: {tupla.index(3) + 1}ª posição')

print(f'Números pares que apareceram: ', end='')
qtdpares = 0
for numero in tupla:
    if numero % 2 == 0:
        print(f'{numero} ', end='')
        qtdpares += 1

if qtdpares == 0:
    print(f'Nenhum')
from random import randint

tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print('Os valores sorteados foram: ', end='')

for c in range(0, len(tupla)):
    print(f'{tupla[c]} ', end='')

print(f'\nMaior valor: {max(tupla)}')
print(f'Menor valor: {min(tupla)}')

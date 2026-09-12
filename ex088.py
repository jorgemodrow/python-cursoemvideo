from random import randint
from time import sleep

print('-'*45)
print(f'{"PALPITEIRO DA MEGA SENA":^45}')
print('-'*45)
matriz = []

jogos = int(input('\nQuantidade de jogos que serão gerados => '))
print()

for c in range(0, jogos):
    matriz.append([])
    for num in range(0,6):
        while True:
            valor = randint(1, 60)
            if valor not in matriz[c]:
                break
        matriz[c].append(valor)

    matriz[c].sort()
    print(f'Jogo {c+1}: {matriz[c]}')
    sleep(0.5)

print(f'\n{" < BOA SORTE! > ":-^45}')
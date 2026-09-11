from random import randint
from time import sleep

palpites = 0
acertou = False
computador = randint(0,10)

print('-=-'*20)
print('Vou pensar em um número inteiro entre 0 e 10.')
print('-=-'*20)

while not acertou:
    palpites += 1
    jogador = int(input('Qual número eu pensei => '))

    if jogador == computador:
        acertou = True
    elif computador < jogador:
        print('Menos... Tente novamente.\n')
    else:
        print('Mais... Tente novamente.\n')

print('Acertou!')
print(f'Foram necessárias {palpites} tentativas')
print(f'O número pensado foi: {computador}')
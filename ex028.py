from random import randint
from time import sleep

computador = randint(0,5)

print('-=-'*20)
print('Vou pensar em um número inteiro entre 0 e 5.')
print('-=-'*20)

jogador = int(input('Qual número eu pensei => '))

print('Processando...')
sleep(2)

if computador == jogador:
    print('Venceu!')
else:
    print('Perdeu!')

print('O número pensado foi: {}'.format(computador))
from random import randint
from time import sleep

itens = ('', 'PEDRA', 'PAPEL', 'TESOURA')

print('''Considerando:

[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA
''')
jogador = int(input('Digite sua jogada: '))
computador = randint(1, 3)

musica = '''
PE
DRA
PAPEL
TE
SOU
RA!!!
'''

for linha in musica.splitlines():
    print(linha)
    sleep(0.3)

print(f'''---------------
Jogador jogou: {itens[jogador]}
Computador jogou: {itens[computador]}
---------------''')

if jogador == computador:
    vencedor = 'EMPATE'
elif (jogador == 1) and (computador == 2):
    vencedor = 'COMPUTADOR'
elif (jogador == 1) and (computador == 3):
    vencedor = 'JOGADOR'
elif (jogador == 2) and (computador == 1):
    vencedor = 'JOGADOR'
elif (jogador == 2) and (computador == 3):
    vencedor = 'COMPUTADOR'
elif (jogador == 3) and (computador == 1):
    vencedor = 'COMPUTADOR'
elif (jogador == 3) and (computador == 2):
    vencedor = 'JOGADOR'
else:
    print('Caractere inválido!')
    vencedor = 'Nenhum jogo'

print(f'Vencedor foi: {vencedor}')


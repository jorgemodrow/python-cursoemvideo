from random import randint

print('-' * 30)
print('JOGO DE PAR OU ÍMPAR')
print('-' * 30)
soma = 0
partidasvencidas = 0

while True:
    parimpar = input('Par ou Ímpar [P/I]: ').upper()
    jogador = int(input('Digite a sua jogada => '))
    computador = randint(0, 10)
    print(f'\nVocê jogou: {jogador}')
    print(f'Computador jogou: {computador}')
    total = jogador + computador
    print(f'Total = {total}')
    if total % 2 == 0:
        print('\nDEU PAR')
    else:
        print('\nDEU IMPAR')

    if (total % 2 == 0 and parimpar == 'P') or (total % 2 == 1 and parimpar == 'I'):
        print('Você VENCEU!')
        partidasvencidas += 1
    else:
        print('Você PERDEU!')
        break

print('-=' * 15)
print('GAME OVER!')
print(f'Você venceu {partidasvencidas} vezes')
def ficha(nome, gols):
    if len(nome) == 0:
        nome = '<desconhecido>'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')

nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)
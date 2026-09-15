jogador = dict()
grupo = list()
gols = list()

print('-'*55)
print(f'{'CADASTRO DE JOGADORES DE FUTEBOL':^55}')
print('-'*55)

while True:
    gols = []
    nome = str(input('Nome do jogador: '))
    partidas = int(input('Quantidade de partidas: '))

    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols feitos na partida {i+1}: ')))

    jogador = {
        'nome': nome,
        'partidas': partidas,
        'gols': gols.copy(),
        'total': sum(gols)
    }

    grupo.append(jogador.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break

    if continuar == 'N':
        break

print('-'*55)
print(f'\n{'cod':>3} {'nome':<20} {'gols':<20} {'total':<5}')
print('-'*55)

for i, j in enumerate(grupo):
    print(f'{i:>3} {j['nome']:<20} {str(j["gols"]):<20} {j['total']:<5}')

while True:
    print('-'*55)
    mostrar = int(input('Mostrar dados de qual jogador (999 encerra) => '))
    if mostrar == 999:
        break
    elif mostrar >= len(grupo):
        print(f'ERRO! Não existe jogador com código {mostrar}! Tente novamente.')
    else:
        print(f'LEVANTAMENTO DO JOGADOR {grupo[mostrar]["nome"]}:')
        for i, v in enumerate(grupo[mostrar]['gols']):
            print(f'    => No jogo {i+1} fez {v} gols.')
jogador = dict()
gols = list()

print('-'*40)
print(f'{'CADASTRO DE UM JOGADOR DE FUTEBOL':^40}')
print('-'*40)

nome = str(input('Nome: '))
partidas = int(input('Quantidade de partidas: '))

for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols feitos na partida {i+1}: ')))

jogador = {
    'nome': nome,
    'partidas': partidas,
    'gols': gols.copy(),
    'total': sum(gols)
}

print('-'*40)
print(jogador)
print('-'*40)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-'*40)
print(f'O jogador {jogador['nome']} jogou {jogador["partidas"]} partidas.')

for k,v in enumerate(jogador['gols']):
    print(f'    => Na partida {k+1} fez {v} gols.')

print(f'Foi um total de {jogador["total"]} gols.')
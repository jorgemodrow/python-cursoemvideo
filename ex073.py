tabela_brasileirao = (
    'Flamengo',
    'Palmeiras',
    'Athletico-PR',
    'Fluminense',
    'Bahia',
    'Cruzeiro',
    'Coritiba',
    'Atlético-MG',
    'Bragantino',
    'São Paulo',
    'EC Vitória',
    'Corinthians',
    'Santos',
    'Botafogo',
    'Grêmio',
    'Mirassol',
    'Vasco da Gama',
    'Internacional',
    'Remo',
    'Chapecoense'
)

print(f'Lista de times do Brasileirão 2026: {tabela_brasileirao}')
print(f'5 primeiros colocados: {tabela_brasileirao[:5]}')
print(f'4 últimos colocados: {tabela_brasileirao[-4:]}')
print(f'Todos os times em ordem alfabética: {sorted(tabela_brasileirao)}')
print(f'A Chapecoense está na {tabela_brasileirao.index("Chapecoense") + 1}ª posição')
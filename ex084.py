pessoa = []
dados = []
cont = 0
continuar = 'S'

while continuar == 'S':
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso (kg): ')))
    pessoa.append(dados[:])
    dados.clear()
    cont += 1
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break

print('-'*40)
print(f'{cont} pessoas foram cadastradas.')

for c in range(0, cont):
    if c == 0:
        maiorpeso = pessoa[0][1]
        menorpeso = pessoa[0][1]
    else:
        if pessoa[c][1] >= maiorpeso:
            maiorpeso = pessoa[c][1]
        elif pessoa[c][1] <= menorpeso:
            menorpeso = pessoa[c][1]

print(f'O maior peso foi de {maiorpeso}kg. Peso de ', end='')

for c in range(0, cont):
    if pessoa[c][1] == maiorpeso:
        print(f'[{pessoa[c][0]}]', end='')

print(f'\nO menor peso foi de {menorpeso}kg. Peso de ', end='')

for c in range(0, cont):
    if pessoa[c][1] == menorpeso:
        print(f'[{pessoa[c][0]}]', end='')
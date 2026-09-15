grupo = list()
mulheres = list()
pessoa = dict()
soma = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))

    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    grupo.append(pessoa.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).upper()
        if continuar == 'N' or continuar == 'S':
            break

    if continuar == 'N':
        break

print('-' * 40)
print(f'- O grupo tem {len(grupo)} pessoas.')

media = soma / len(grupo)
print(f'- A média de idade é de {media:5.2f} anos.')

print(f'- As mulheres cadastradas foram: ', end='')
for p in grupo:
    if p['sexo'] == 'F':
        print(f'{pessoa["nome"]} ', end='')

print(f'\n- Lista das pessoas que estão acima da média:')

for p in grupo:
    if p['idade'] >= media:
        for k,v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('\n<< ENCERRADO >>')
estatistica1 = estatistica2 = estatistica3 = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        estatistica1 += 1

    if sexo == 'M':
        estatistica2 += 1

    if sexo == 'F' and idade < 20:
        estatistica3 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print(f'Quantidade de pessoas com mais de 18 anos: {estatistica1}')
print(f'Quantidade de homens que foram cadastrados: {estatistica2}')
print(f'Quantidade de mulheres com menos de 20 anos: {estatistica3}')
sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Inválido. Informe novamente seu sexo [M/F]: ')).strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso!')
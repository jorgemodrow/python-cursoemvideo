alunos = []
continuar = 'S'
i = 0
while continuar == 'S':
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    i += 1
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break

print('-'*50)
print(f'{'N°':<3}{'Nome':<15}{'Média':<5}')
print('-'*50)
for c in range(0,i):
    print(f'{c:<3}{alunos[c][0]:<15}{alunos[c][2]:<5}')

print('-'*50)
while True:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    else:
        if mostrar <= len(alunos) - 1:
            print(f'As notas de {alunos[mostrar][0]} foram {alunos[mostrar][1]}')
        else:
            print('Aluno inválido!')
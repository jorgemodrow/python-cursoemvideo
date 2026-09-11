n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
media = (n1 + n2) / 2

print(f'Média do aluno: {media:.1f}')

if media < 5:
    print('O aluno está REPROVADO')
elif media < 6.9:
    print('O aluno está EM RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')
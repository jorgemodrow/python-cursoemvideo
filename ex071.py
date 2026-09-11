print('CAIXA ELETRÔNICO - SAQUE')
saque = int(input('Qual o valor do saque? R$ '))

notas50 = 0
notas20 = 0
notas10 = 0
notas1 = 0

while saque >= 50:
    notas50 += 1
    saque -= 50

while saque >= 20:
    notas20 += 1
    saque -= 20

while saque >= 10:
    notas10 += 1
    saque -= 10

while saque >= 1:
    notas1 += 1
    saque -= 1

print(f'''Total de {notas50} notas de R$ 50
Total de {notas20} notas de R$ 20
Total de {notas10} notas de R$ 10
Total de {notas1} notas de R$ 1''')
numero = int(input('Digite um número inteiro: '))

print('''
TABUADA
-----------''')
for i in range(1, 11):
    print(f'{numero} * {i} = {numero * i}')
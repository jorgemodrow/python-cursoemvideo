cont = 0
soma = 0
num = int(input('Digite um número inteiro (999 para parar): '))

while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número inteiro (999 para parar): '))

print(f'Quantidade de números digitados: {cont}')
print(f'Soma dos números digitados: {soma}')



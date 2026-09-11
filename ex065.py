num = int(input('Digite um número: '))
maior = menor = num
soma = num
cont = 1
res = str(input('CONTINUAR [S/N]: ').upper())
print()

while res == 'S':
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    else:
        menor = num

    soma += num
    cont += 1

    res = str(input('CONTINUAR [S/N]: ').upper())
    print()

media = soma / cont
print(f'Quantidade de números digitados: {cont}')
print(f'Média dos valores: {media:.2f}')
print(f'Maior: {maior}')
print(f'Menor: {menor}')
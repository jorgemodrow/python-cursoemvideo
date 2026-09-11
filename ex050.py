soma = 0
cont = 0

for i in range(1, 7):
    valor = int(input(f'Digite o valor {i}/6: '))
    if valor % 2 == 0:
        soma += valor
        cont += 1

print()
print(f'A soma dos {cont} valores PARES digitados é: {soma}')
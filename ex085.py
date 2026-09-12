lista = [[], []]

for c in range(0, 7):
    dado = int(input(f'Digite o valor [{c+1}/7]: '))
    if dado % 2 == 0:
        lista[0].append(dado)
    else:
        lista[1].append(dado)

lista[0].sort()
lista[1].sort()

print(f'Valores pares digitados: {lista[0]} ')
print(f'Valores impares digitados: {lista[1]}')
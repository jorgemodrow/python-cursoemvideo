soma = 0
cont = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        cont += 1

print(f'''Considerando:

- Números ímpares
- Múltiplos de 3
- Estão no intervalo de 1 até 500

A soma de todos os {cont} números é {soma}''')
num = int(input('Digite um número para mostrar seu fatorial: '))
res = 1
print('-=-'*20)
print(f'Calculando: {num}! = ', end='')
while num != 0:
    print(f'{num}', end='')
    res *= num
    num -= 1

    if num != 0:
        print(' * ', end='')

print()
print('-=-'*20)
print(f'Resultado: {res}')
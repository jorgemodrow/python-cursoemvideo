numero = int(input("Digite um número inteiro para ver seus divisores: "))
tot = 0
primo = True

for c in range(1, numero+1):
    if numero % c == 0:
        if c != 1 and c != numero:
            primo = False
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')

    print(f'{c} ', end='')

print(f'\n\033[mO número {numero} foi divisível {tot} vezes')
if primo == True:
    print('É primo!')
else:
    print('Não é primo!')
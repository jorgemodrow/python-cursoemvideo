numero = int(input('Digite um numero inteiro: '))

print('''Considerando:

[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL
''')
base = int(input('Digite uma opção de conversão: '))

if base == 1:
    print(f'Binário: {bin(numero)[2:]}')
elif base == 2:
    print(f'Octal: {oct(numero)[2:]}')
elif base == 3:
    print(f'Hexadecimal: {hex(numero)[2:]}')
else:
    print('Digite uma opção válida')
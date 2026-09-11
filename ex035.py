a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))

if a < b + c and b < a + c and c < a + b:
    print('Os valores acima podem formar um triângulo!')
else:
    print('Os valores acima não podem formar um triângulo!')
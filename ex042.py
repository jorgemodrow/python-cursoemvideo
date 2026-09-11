a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))

if a < b + c and b < a + c and c < a + b:
    print('Os valores acima podem formar um triângulo!')

    if a == b == c:
        tipotriangulo = 'EQUILÁTERO'
    elif a != b != c != a != c != b:
        tipotriangulo = 'ESCALENO'
    else:
        tipotriangulo = 'ISÓSCELES'

    print(f'Tipo de triângulo: {tipotriangulo}')
else:
    print('Os valores acima não podem formar um triângulo!')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    maior = a
elif b > c and b > a:
    maior = b
else:
    maior = c

if a < b and a < c:
    menor = a
elif b < c and b < a:
    menor = b
else:
    menor = b

print('Menor => {}'.format(menor))
print('Maior => {}'.format(maior))
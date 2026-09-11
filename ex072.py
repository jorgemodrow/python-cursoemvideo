extenso = (
    'zero', 'um', 'dois', 'três', 'quatro',
    'cinco', 'seis', 'sete', 'oito', 'nove',
    'dez', 'onze', 'doze', 'treze', 'catorze',
    'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove',
    'vinte'
)

while True:
    indice = int(input('Digite um número de 0 a 20: '))
    if indice < 0 or indice > 20:
        print('Tente novamente!', end=' ')
    else:
        break

print(f'Você digitou o número {extenso[indice]}')
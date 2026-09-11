produtos = ('Teclado Mecânico', 250.00,
            'Mouse Gamer', 120.00,
            'Monitor 24"', 750.00,
            'Headset USB', 180.00,
            'SSD 1TB', 320.00,
            'Computador Gamer', 4120.00)

print('-' * 40)
print(f'{"TABELA DE PRODUTOS":^40}')
print('-' * 40)

for i in range(0,len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end='')
    else:
        print(f'R${produtos[i]:>8.2f}')
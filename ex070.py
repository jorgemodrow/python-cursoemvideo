print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)

totalgasto = 0
totalmil = 0
menor = 0
nomemenor = ''
cont = 0
while True:
    nomeproduto = str(input('Nome do produto: ')).strip().upper()
    precoproduto = int(input('Preço do produto: R$ '))
    cont += 1
    totalgasto += precoproduto

    if precoproduto > 1000:
        totalmil += 1

    if cont == 1 or precoproduto < menor:
        menor = precoproduto
        nomemenor = nomeproduto

    if precoproduto < menor:
        menor = precoproduto
        nomemenor = nomeproduto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break

print('-' * 20)
print(f'Total da compra: R$ {totalgasto:.2f}')
print(f'Produtos com valor acima de R$ 1000: {totalmil}')
print(f'O produto mais barato foi {nomemenor}, custando R$ {menor:.2f}')
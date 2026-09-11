distancia = int(input('Digite a distância da viagem em km: '))
if distancia <= 200:
    preco = 0.50 * distancia
else:
    preco = 0.45 * distancia
print('Valor da viagem: R$ {:.2f}'.format(preco))
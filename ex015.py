print('=== SISTEMA DE ALUGUEL DE CARROS ===')
dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos km o carro rodou enquanto foi alugado: '))
preco = dias * 60 + km * 0.15
print('O total a pagar é de R$ {:.2f}'.format(preco))

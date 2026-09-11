valor = float(input('Digite o valor do produto => R$ '))

print('''Considerando:

[ 1 ] À vista (dinheiro/cheque)
[ 2 ] À vista (cartão)
[ 3 ] 2x (cartão)
[ 4 ] 3x ou mais (cartão)
''')
formapagamento = int(input('Digite a forma de pagamento: '))

if formapagamento == 1:
    novovalor = valor * 0.90
elif formapagamento == 2:
    novovalor = valor * 0.95
elif formapagamento == 3:
    novovalor = valor
elif formapagamento == 4:
    novovalor = valor * 1.2
else:
    print('Opção inválida!')

print(f'\nO valor do produto, nessa forma de pagamento, fica: R$ {novovalor:.2f}')
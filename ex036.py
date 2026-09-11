print('PROGRAMA CALCULADOR DE EMPRÉSTIMO BANCÁRIO')
print('Finalidade: compra de um imóvel\n')

valordacasa = float(input('Digite o valor do imóvel: R$ '))
salariocomprador = float(input('Digite o salário do comprador: R$ '))
anosquitacao = int(input('Em quantos anos deseja pagar: '))

limiteprestacao = salariocomprador * 0.30
mesesquitacao = anosquitacao * 12
prestacao = valordacasa / mesesquitacao

if ( prestacao <= (salariocomprador*0.30) ):
    print('\nEMPRÉSTIMO CONCEDIDO!')
    print(f'Valor das parcelas: R$ {prestacao:.2f}')
else:
    print('\nEMPRÉSTIMO NEGADO!')
    print(f'Valor da parcela: R$ {prestacao:.2f}')
    print(f'Valor máximo da parcela: R$ {limiteprestacao:.2f} (30% do salário)')

    while prestacao > limiteprestacao:
        mesesquitacao += 1
        prestacao = valordacasa / mesesquitacao

    anos_necessarios = mesesquitacao / 12

    print(f'\nPara ser aprovado, você precisaria financiar em {mesesquitacao} meses (cerca de {anos_necessarios:.1f} anos).')
    print(f'Nova parcela ajustada: R$ {prestacao:.2f}')
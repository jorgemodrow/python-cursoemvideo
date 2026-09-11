velocidade = float(input('Informe a velocidade: '))
if velocidade > 80:
    print('Você foi multado!')
    multa = (velocidade - 80) * 7
    print('Valor da multa: R$ {:.2f}'.format(multa))

print('Tenha um bom dia! Dirija com segurança')
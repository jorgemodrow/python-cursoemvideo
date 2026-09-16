def escreva(texto):
    tam = len(texto)+2
    print('-'*tam)
    print(f'{texto:^{tam}}')
    print('-'*tam)

# Programa Principal
mensagem = str(input('Digite uma mensagem: '))
escreva(mensagem)
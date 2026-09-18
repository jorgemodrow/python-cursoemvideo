def metade(valor, converter=True):
    res = valor / 2
    if converter == True:
        res = moeda(res)
    return res

def dobro(valor, converter=True):
    res = valor * 2
    if converter == True:
        res = moeda(res)
    return res
def aumentar(valor, aumento, converter=True):
    res = valor + (valor * aumento/100)
    if converter == True:
        res = moeda(res)
    return res

def diminuir(valor, reducao, converter=True):
    res = valor - (valor * reducao/100)
    if converter == True:
        res = moeda(res)
    return res

def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')

def resumo(valor, aumento, reducao):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-'*30)
    print(f'{"Preço analisado:":<20}{moeda(valor)}')
    print(f'{"Dobro do preço:":<20}{dobro(valor, True)}')
    print(f'{"Metade do preço:":<20}{metade(valor, True)}')
    print(f'{f"{aumento}% de aumento:":<20}{aumentar(valor, aumento, True)}')
    print(f'{f"{reducao}% de redução:":<20}{diminuir(valor, reducao, True)}')
    print('-'*30)

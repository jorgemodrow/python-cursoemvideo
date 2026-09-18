def metade(valor, converter=False):
    res = valor / 2
    if converter == True:
        res = moeda(res)
    return res

def dobro(valor, converter=False):
    res = valor * 2
    if converter == True:
        res = moeda(res)
    return res
def aumentar(valor, mult, converter=False):
    res = valor + (valor * mult/100)
    if converter == True:
        res = moeda(res)
    return res

def diminuir(valor, mult, converter=False):
    res = valor - (valor * mult/100)
    if converter == True:
        res = moeda(res)
    return res

def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')
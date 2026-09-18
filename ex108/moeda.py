def metade(valor):
    return valor / 2

def dobro(valor):
    return valor * 2
def aumentar(valor, mult):
    porcent = mult / 100
    return valor * ( 1 + porcent)

def diminuir(valor, mult):
    porcent = mult / 100
    return valor * (1 - porcent)

def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')
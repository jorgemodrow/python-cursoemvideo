from datetime import datetime

def voto(anonasc):
    idade = datetime.now().year - anonasc
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('NÃO VOTA')
    elif idade < 18 or idade > 65:
        print('VOTO OPCIONAL')
    else:
        print('VOTO OBRIGATORIO')

anonasc = int(input('Em que ano você nasceu? '))
voto(anonasc)
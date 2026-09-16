c = ('\033[m',   # 0 Sem cor
     '\033[34m', # 1 Azul
     '\033[33m', # 2 Amarelo
     '\033[31m'  # 3 Vermelho
    )

def titulo(texto, cor=0):
    largura = len(texto)+4
    print(c[cor], end='')
    print('-'*largura)
    print(f'{texto:^{largura}}')
    print('-'*largura, end=f'{c[0]}\n')

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 1)

    comando = str(input('Função ou Biblioteca ("FIM" encerra) > ')).lower()

    if comando != 'fim':
        titulo(f'Acessando o manual do comando `{comando}`', 2)
        help(comando)
    else:
        titulo('ATÉ LOGO!', 3)
        break
def leiaDinheiro(msg):
    while True:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO: "{entrada}" é um preço inválido!\033[m')
        else:
            res = float(entrada)
            break
    return res
def leiaInt(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[0m')

    return n

valor = leiaInt('Digite um número inteiro: ')

print(f'Você acabou de digitar o número {valor}')
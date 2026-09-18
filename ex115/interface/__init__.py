def selecionar(p):
    while True:
        try:
            opt = int(input(p))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
        else:
            if opt < 1 or opt > 3:
                print('ERRO: por favor, digite uma opção válida')
            else:
                return opt
                break

def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[0;31mERRO! O valor tem que ser inteiro.\033[m')
        except (KeyboardInterrupt):
            print(f'\n\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            num = 0
            break
        else:
            break
    return num
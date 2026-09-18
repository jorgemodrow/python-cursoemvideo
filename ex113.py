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

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except TypeError:
            print(f'\033[0;31mERRO! O valor tem que ser inteiro.\033[m')
        except ValueError:
            print(f'\033[0;31mUsuário preferiu não digitar esse número.\033[m')
            num = 0
            break
        else:
            break
    return num


# Programa principal

int = leiaInt('Digite um valor inteiro: ')
float = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {int} e o real foi {float}.')


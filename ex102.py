
def fatorial(num=1, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: O número a ser calculado o fatorial
    :param show: (opcional) mostrar ou não a conta
    :return: o valor do fatorial de um número num
    """
    res = 1
    for c in range(num, 0, -1):
        res *= c
        if show:
            if c == num:
                print(f'{num} ', end='')
            elif c > 1:
                print(f'x {c} ', end='')
            else:
                print(f'x {c} = ', end='')

    return res


numero = int(input('Digite um número para mostrar seu fatorial: '))
show = True
print(fatorial(numero,show))
print('-'*30)
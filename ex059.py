n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0

while opcao != 5:
    opcao = int(input('''\nDadas as opções:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Entrar com novos números
    [5] Sair
    
    Digite a opção desejada: '''))

    if opcao == 1:
        res = n1 + n2
        print(f'\nResultado: {res}\n')
    elif opcao == 2:
        res = n1 * n2
        print(f'\nResultado: {res}\n')
    elif opcao == 3:
        if n1 > n2:
            res = n1
        else:
            res = n2
        print(f'\nResultado: {res}\n')
    elif opcao == 4:
        n1 = int(input('\nPrimeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('\nFinalizando...')
    else:
        print('\nOpção inválida, tente novamente')


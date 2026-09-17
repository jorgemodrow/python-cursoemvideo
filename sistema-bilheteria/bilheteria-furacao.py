letravermelha = '\033[31m'
semfundo = '\033[0m'
setor = ('RED (Laterais do campo)',
         'FAN (Atrás do gol/Fanáticos)',
         'GOLD (Setores superiores)',
         'VISITANTE (Espaço destinado à torcida adversária)',
         'BLACK / VIP (Área central inferior com cadeiras estofadas)',
         'CHOPERIA ARENA BRAHMA (Área VIP temática)')
tipoingresso = ('Sócio Furacão', 'Meia-entrada', 'Inteira')
valorsetor = (150.00, 150.00, 150.00, 150.00, 300.00, 300.00)
torcedor = []

def leiaInt(txt):
    while True:
        res = input(txt)
        if res.isnumeric():
            break
        else:
            print(f'{letravermelha}ERRO! Digite um número inteiro válido.{semfundo}')

    return int(res)

def titulo(texto):
    print(f'{letravermelha}=' * 40)
    print(f'{texto:^40}')
    print(f'=' * 40, f'{semfundo}')

def emitiringresso():
    global torcedor
    titulo('EMITIR INGRESSO')

    nome = str(input('Informe o nome do torcedor => ')).title()

    print('\nSETORES DISPONÍVEIS:\n')
    for i in range (0, len(setor)):
        print(f'[{i}] {setor[i]}: R$ {valorsetor[i]:.2f}')

    while True:
        setortorc = int(input('\nEscolha um setor => '))
        if setortorc >= 0 and setortorc < len(setor):
            break
        else:
            print(f'Inválido! Por favor escolha um número de 0 a {len(setor)-1}.')

    print('\n[0] Sócio Furacão\n[1] Meia-entrada\n[2] Inteira\n')

    while True:
        tipoingressotorcedor = leiaInt('Escolha o tipo do ingresso: ')
        if tipoingressotorcedor == 0 or tipoingressotorcedor == 1:
            valor = valorsetor[setortorc] * 0.5
            break
        elif tipoingressotorcedor == 2:
            valor = valorsetor[setortorc]
            break
        else:
            print('Inválido! Por favor selecione 0, 1 ou 2.')

    torcedor.append([nome, setortorc, tipoingressotorcedor, valor])

    print()
    titulo(f'INGRESSO Nº {len(torcedor)-1} CONFIRMADO!')
    print(f'{letravermelha}Nome: {semfundo}{torcedor[len(torcedor)-1][0]}')
    print(f'{letravermelha}Setor: {semfundo}{setor[torcedor[len(torcedor)-1][1]]}')
    print(f'{letravermelha}Tipo: {semfundo}{tipoingresso[torcedor[len(torcedor)-1][2]]}')
    print(f'{letravermelha}Valor: {semfundo}R$ {torcedor[len(torcedor)-1][3]:.2f}')

    continuar = input('\nDigite algo para voltar ao menu: ')
    print()

def cancelaringresso():
    titulo('CANCELAR INGRESSO')

    if len(torcedor) != 0:
        for i in range (0, len(torcedor)):
            if torcedor[i] != None:
                print(f'[{i}] {torcedor[i][0]}')

        while True:
            opcao = leiaInt('\nDigite um ingresso para cancelar (999 para voltar ao menu) => ')
            if opcao == 999:
                print()
                break
            elif opcao >= 0 and opcao < len(torcedor):
                torcedor[opcao] = None
                print(f'Ingresso [{opcao}] cancelado com sucesso!')
            else:
                print(f'{letravermelha}Inválido! Selecione um número das opções.{semfundo}')
    else:
        print('Não há nenhum ingresso para cancelar!')

def relatoriodetorcedores():
    titulo('RELATÓRIO DE TORCEDORES')

    if len(torcedor) != 0:
        for i in range(0, len(torcedor)):
            print(f'INGRESSO Nº {i}')
            if torcedor[i] != None:
                print(f'Nome: {torcedor[i][0]}')
                print(f'Setor: {setor[torcedor[i][1]]}')
                print(f'Tipo do ingresso: {tipoingresso[torcedor[i][2]]}')
                print(f'Valor do ingresso: R$ {torcedor[i][3]:.2f}\n')
            else:
                print('Nulo!\n')

        i = 1
        while i <= len(torcedor):
            if torcedor[-i] != None:
                print(f'{letravermelha}>> ÚLTIMO INGRESSO VENDIDO: {torcedor[-i][0]} <<{semfundo}\n')
                break
            else:
                i += 1
    else:
        print('Ainda não há nenhum torcedor cadastrado!\n')

    continuar = input('Digite algo para voltar ao menu: ')
    print()

def encerrar():
    titulo('RELATÓRIO FINAL DA ARENA')

    valores_validos = []
    socios_furacao = 0

    for ingresso in torcedor:
        if ingresso != None:
            valores_validos.append(ingresso[3])
            if ingresso[2] == 0:
                socios_furacao += 1

    total_vendidos = len(valores_validos)

    if total_vendidos > 0:
        faturamento = sum(valores_validos)  # sum() soma todos os itens de uma lista
        media = faturamento / total_vendidos
        mais_caro = max(valores_validos)  # max() pega o maior valor
        mais_barato = min(valores_validos)  # min() pega o menor valor

        print(f'Total de ingressos vendidos: {total_vendidos}')
        print(f'Faturamento total: R$ {faturamento:.2f}')
        print(f'Valor médio pago por ingresso: R$ {media:.2f}')
        print(f'Ingresso mais caro: R$ {mais_caro:.2f}')
        print(f'Ingresso mais barato: R$ {mais_barato:.2f}')
        print(f'Quantidade de Sócios Furacão: {socios_furacao}')
    else:
        print('Nenhum ingresso válido foi vendido nesta sessão.')

    print()
    titulo('SISTEMA ENCERRADO')
    exit()


# Programa Principal
while True:
    titulo('SISTEMA DE BILHETERIA FURACÃO')

    print('''
[1] Emitir ingresso
[2] Cancelar ingresso
[3] Relatório de torcedores
[4] Fechar caixa
    ''')

    while True:
        opcao = leiaInt('Escolha uma opção => ')
        if opcao == 1:
            print()
            emitiringresso()
            break
        elif opcao == 2:
            print()
            cancelaringresso()
            break
        elif opcao == 3:
            print()
            relatoriodetorcedores()
            break
        elif opcao == 4:
            print()
            encerrar()
        else:
            print(f'{letravermelha}Opção inválida! Por favor, tente novamente.{semfundo}')
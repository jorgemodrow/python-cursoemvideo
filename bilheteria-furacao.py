letravermelha = '\033[31m'
semfundo = '\033[0m'
setor = ('RED (Laterais do campo)',
         'FAN (Atrás do gol/Fanáticos)',
         'GOLD (Setores superiores)',
         'VISITANTE (Espaço destinado à torcida adversária)',
         'BLACK / VIP (Área central inferior com cadeiras estofadas)',
         'CHOPERIA ARENA BRAHMA (Área VIP temática)')
valorsetor = (150.00, 150.00, 150.00, 150.00, 300.00, 300.00)
torcedor = []

def menu():
    print(f'{letravermelha}='*40, f'{semfundo}')
    print(f'{letravermelha}{'SISTEMA DE BILHETERIA FURACÃO':^40}', f'{semfundo}')
    print(f'{letravermelha}='*40, f'{semfundo}')

    print('''
[1] Emitir ingresso
[2] Cancelar ingresso
[3] Relatório de torcedores
[4] Fechar caixa
    ''')

    opcao = int(input('Escolha uma opção => '))

    print()
    if opcao == 1:
        emitiringresso()

def emitiringresso():
    print(f'{letravermelha}=' * 40, f'{semfundo}')
    print(f'{letravermelha}{'EMITIR INGRESSO':^40}', f'{semfundo}')
    print(f'{letravermelha}=' * 40, f'{semfundo}')

    torcedor.append(str(input('\nInforme o nome do torcedor => ')).title())

    print('\nSETORES:\n')
    for i in range (0, len(setor)):
        print(f'[{i}] {setor[i]}')
    
    torcedor.append(int(input('\nEscolha um setor => ')))

    print('''
[S] Sócio Furacão
[M] Meia-entrada
[I] Inteira
    ''')
    tipoingressotorcedor = str(input('Selecione o tipo do ingresso: ').upper())
    if tipoingressotorcedor in 'SM':
        torcedor.append(valorsetor[torcedor[1]] * 0.5)
    else:
        torcedor.append(valorsetor[torcedor[1]])

    print(f'{letravermelha}=' * 40, f'{semfundo}')
    print(f'{letravermelha}{'INGRESSO CONFIRMADO!':<40}', f'{semfundo}')
    print(f'{letravermelha}{f'Nome: {torcedor[0]} | Setor: {setor[torcedor[1]]} | Valor: R$ {torcedor[2]:.2f}':^40}', f'{semfundo}')
    print(f'{letravermelha}=' * 40, f'{semfundo}')

if __name__ == '__main__':
    menu()
from venv import create

from ex115.interface import *
from ex115.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    print('-'*40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('-'*40)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar uma pessoa')
    print('3 - Sair do sistema')
    print('-'*40)
    opcao = selecionar('Sua Opção: ')
    if opcao == 1:
        lerArquivo(arq)
    elif opcao == 2:
        print('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    else:
        print('Saindo do sistema... Até logo!')
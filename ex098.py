from time import sleep

def contador(ini,fim,pas):
    if pas < 0:
        pas = pas - pas - pas
    elif pas == 0:
        pas = 1

    print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
    if fim < ini:
        for c in range(ini,fim-1,-pas):
            print(f'{c} ',end='', flush=True)
            sleep(0.25)
    else:
        for c in range(ini,fim+1,pas):
            print(f'{c} ',end='', flush=True)
            sleep(0.25)
    print('FIM!')
    print('-' * 40)

print('-'*40)
contador(1,10,1)
contador(10,0,2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)
print('PROGRESSÃO ARITMÉTICA')

primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeirotermo
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} → ', end='')
        termo += razao
        cont +=1

    print('PAUSA')
    mais = int(input('Quantos termos a mais: '))

print(f'FIM! Progressão finalizada com {total} termos mostrados.')
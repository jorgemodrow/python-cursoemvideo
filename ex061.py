print('PROGRESSÃO ARITMÉTICA')

primeirotermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeirotermo
cont = 1

while cont <= 10:
    print(f'{termo} → ', end='')
    termo += razao
    cont +=1
print('FIM')
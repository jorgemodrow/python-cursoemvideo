expressao = str(input('Digite uma expressão matemática: '))
valido = True
cont = 0

for i in range(0,len(expressao)):
    if expressao[i] == '(':
        cont += 1
    elif expressao[i] == ')':
        cont -= 1

    if cont < 0:
        valido = False
        break

if cont > 0:
    valido = False

if valido:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')
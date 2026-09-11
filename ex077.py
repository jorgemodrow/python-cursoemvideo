palavras = ('python', 'programar', 'linguagem', 'computador', 'teclado', 'grrr')

for p in palavras:
    totalvogais = 0
    print(f'\nNa palavra "{p.upper()}" temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
            totalvogais += 1

    if totalvogais == 0:
        print('nenhuma vogal encontrada.', end='')
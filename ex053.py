frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')

fraseaocontrario = ''

for letra in range(len(frase)-1, -1, -1):
    fraseaocontrario += frase[letra]

if frase == fraseaocontrario:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')
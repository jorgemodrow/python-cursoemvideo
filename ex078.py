lista = []

for c in range(0, 5):
    lista.append(int(input(f'Digite o número {c + 1}/5: ')))

menor = min(lista)
maior = max(lista)

print(f'Menor valor: {menor} ({lista.index(menor) + 1}ª posição)')
print(f'Maior valor: {maior} ({lista.index(maior) + 1}ª posição)')
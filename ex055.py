for c in range(1, 6):
    peso = float(input(f'Digite um peso da pessoa {c}/5: '))

    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Maior peso: {maior}')
print(f'Menor peso: {menor}')


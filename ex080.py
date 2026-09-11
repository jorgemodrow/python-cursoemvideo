lista = []

for c in range(1, 6):
    num = int(input(f'Digite o número {c}/5: '))

    if c == 1 or num > lista[-1]:
        lista.append(num)
        print(f'Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print(lista)
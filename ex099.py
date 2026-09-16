def maior(*valores):
    pos = 0
    while pos < len(valores):
        print(f'{valores[pos]} ', end='')
        pos += 1
    print(f'\nForam passados {len(valores)} valores ao todo.\nO maior valor é {max(valores)}')

maior(0,1,2,3,4,55)
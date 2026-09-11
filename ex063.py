num = int(input('Quantos termos deseja mostrar: '))
seq = []
i = 0
while i != num:
    if i == 0:
        seq.append(0)
        print(f'{seq[i]}', end=' → ')
    elif i == 1:
        seq.append(1)
        print(f'{seq[i]}', end=' → ')
    else:
        seq.append(seq[i-1] + seq[i-2])
        print(f'{seq[i]}', end=' → ')
    i+=1
print('FIM')
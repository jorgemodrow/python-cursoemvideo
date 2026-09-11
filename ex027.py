nome_completo = str(input('Digite seu nome completo: ')).strip()
nomes = nome_completo.split()
print('O seu primeiro nome é {}'.format(nomes[0]))
print('O seu último nome é {}'.format(nomes[len(nomes)-1]))

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura
tinta = area / 2
print('Para pintar uma parede de {}x{}, sendo uma área total de {} m², são necessários {} litros de tinta.'.format(largura, altura, area, tinta))
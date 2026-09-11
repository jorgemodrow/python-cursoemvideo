valor = 5968.42
cores = { 'limpa':'\033[m',
          'verde':'\033[1;32m',
          'vermelho':'\033[1;31m' }
print('Sua receita é de: {} R$ {:.2f} {}'.format(cores['verde'], valor, cores['limpa']))
print('Sua dívida é de: {} R$ {:.2f}'.format(cores['vermelho'], valor))
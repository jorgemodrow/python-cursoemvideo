from datetime import datetime

trabalhador = dict()

trabalhador['nome'] = str(input('Nome: '))
anonasc = int(input('Ano de nascimento: '))
trabalhador['idade'] = datetime.now().year - anonasc
trabalhador['cpts'] = int(input('Carteira de trabalho (digite "0" se não tiver): '))

if trabalhador['cpts'] != 0:
    trabalhador['contratacao'] = int(input('Ano de contratação: '))
    trabalhador['aposentadoria'] = trabalhador['contratacao'] + 35 - anonasc
    trabalhador['salario'] = float(input('Salário: R$ '))

print('-'*40)
print(trabalhador)
for k,v in trabalhador.items():
    print(f'{k} tem o valor {v}')
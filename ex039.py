from datetime import date
anoatual = date.today().year
anonascimento = int(input('Digite o ano de nascimento: '))
idade = anoatual - anonascimento

if idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
    print(f'Seu alistamento será em {anoatual+saldo}')
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
else:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos')

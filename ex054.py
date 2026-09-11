import datetime

maioridade = 0
anoatual = datetime.date.today().year

for c in range(1, 8):
    anonasc = int(input(f'Digite o ano de nascimento da pessoa {c}/7: '))
    if anoatual - anonasc >= 18:
        maioridade += 1

print(f'''
De 7 pessoas:
{maioridade} atingiram a maioridade
{7 - maioridade} ainda não atingiram a maioridade''')
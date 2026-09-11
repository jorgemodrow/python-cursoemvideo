nome = []
idade = []
sexo = []
mdado = 0 # idade do homem mais velho
nomevelho = '' # nome do homem mais velho
fdado = 0 # quantidade de mulheres com menos de 20 anos

# Estilos de texto
RESET = "\033[0m"
NEGRITO = "\033[1m"

# Efeito Marca-Texto (Cores de Fundo)
FUNDO_AMARELO = "\033[43;30m" # O ';30' deixa a letra preta para dar mais contraste
FUNDO_VERDE = "\033[42;30m"
FUNDO_CIANO = "\033[46;30m"

for c in range(1, 5):
    print(f"DADOS DA PESSOA {c} de 4")
    nome.append(str(input('Nome: ')).strip())
    idade.append(int(input('Idade: ')))
    sexo.append(str(input('Sexo [M/F]: ')).strip().upper())
    print()

mediaidade = sum(idade) / 4

for c in range(0, 4):
    if sexo[c] == 'M':
        homem = True
        if idade[c] > mdado:
            mdado = idade[c]
            nomevelho = nome[c]
    elif sexo[c] == 'F':
        if idade[c] < 20:
            fdado += 1

# Exibindo os resultados com efeito marca-texto
print(f'Média de idade desse grupo: {NEGRITO}{FUNDO_CIANO} {mediaidade} anos {RESET}')

if nomevelho != '':
    print(f'Nome do homem mais velho: {NEGRITO}{FUNDO_AMARELO} {nomevelho}, com {mdado} anos {RESET}')
else:
    print('Nome do homem mais velho: Nesses dados não há homens.')

print(f'Quantidade de mulheres com menos de 20 anos: {NEGRITO}{FUNDO_VERDE} {fdado} {RESET}')

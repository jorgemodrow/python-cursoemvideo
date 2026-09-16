def notas(*n, sit=False):
    """
    Função recebe uma sequência de notas e retorna um dicionário com o total, maior, menor e média das notas.
    :param n: sequência de notas
    :param sit: situação geral da notas
    :return: dicionário com dados das notas
    """
    media = sum(n) / len(n)
    dados = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': media}
    if sit:
        if media >= 7:
            dados['sit'] = 'BOA'
        elif media >= 5:
            dados['sit'] = 'RAZOÁVEL'
        else:
            dados['sit'] = 'RUIM'

    return dados
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
import urllib.request
import urllib.error

try:
    # Criamos a requisição informando um User-Agent de navegador
    req = urllib.request.Request(
        'http://pudim.com.br',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    # Executamos a requisição com o "disfarce"
    site = urllib.request.urlopen(req)

except urllib.error.URLError:
    print('\033[0;31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[0;32mConsegui acessar o site Pudim com sucesso!\033[m')
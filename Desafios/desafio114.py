import requests

url = "https://www.youtube.com/watch?v=qLuc8kZty1A"

try:
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        print('O site YOUTUBE esta acessivel.')
    else:
        print('O site Youtube nao esta acessivel, mas foi possivel alcanca-lo.')
except requests.exceptions.RequestException as e:
    print(' O site Youtube nao esta acessivel. ERRO: ', e)
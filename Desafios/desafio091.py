from random import randint
from time import sleep
from operator import itemgetter
jogo = { 'jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6),
        'jogador5': randint(1, 6)}
ranking = list()
print("-" * 50)
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('=' * 50)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1} Lugar: {v[0]} com {v[1]}')
    sleep(1)
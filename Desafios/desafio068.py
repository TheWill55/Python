from random import randint
from colorama import Fore, Style, init
print('-' * 30)
print('Vamos jogar par ou impar!')
print('-' * 30)
v = 0
while True:
    jogador = int(input('Escolha seu número: '))
    pc = randint(0,10)
    total = jogador + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I] ')).strip().upper() [0]
    print(f'Você jogou {jogador} e o computador jougou {pc}, total =  {total}', end=' ')
    print('\033[1;36m!Deu par!\033[0m' if total % 2 == 0 else '\033[1;36m!Deu impar!\033[0m')
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[1;32m**Você Ganhou!**\033[0m')
            v += 1
        else:
            print('\033[1;31m**Você Perdeu!**\033[0m')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[1;32m**Você Ganhou!**\033[0m')
            v += 1
        else:
            print('\033[1;31m**Você Perdeu!**\033[0m')
            break
    print('Vamos jogar novamente!')
print(f'\033[1;34mFim da jogada! Total de vitórias: {v}\033[0m')

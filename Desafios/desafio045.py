from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Escolha sua jogada
      [0] Pedra
      [1] Papel
      [2] Tesoura ''')
jogador = int (input('qual é sua jogada :'))
print('JO!')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
print('-' * 40)
print('O computador jogou {}'.format(itens[computador]))
print('Você escoulheu {}'.format(itens[jogador]))
print('-' * 40)
if computador == 0:
    if jogador == 0:
        print('\033[7;34mEmpate!\033[0m')
    elif jogador == 1:
        print('\033[1;32mVoçê GANHOU!!!\033[0m')
    elif jogador == 2:
        print('\033[1;33mVoce PERDEU!!!\033[0m')
    else:
        print('\033[7;31mERRO\033[1;31mJogada invalida!\033[0m')
elif computador == 1:
    if jogador == 0:
          print('\033[1;33mVoce PERDEU!!!\033[0m')
    elif jogador == 1:
        print('\033[7;34mEmpate!\033[0m')
    elif jogador == 2:
        print('\033[1;32mVoçê GANHOU!!!\033[0m')
    else:
        print('\033[7;31mERRO\033[1;31mJogada invalida!\033[0m')
elif computador == 2:
    if jogador == 0:
        print('\033[1;32mVoçê GANHOU!!!\033[0m')
    elif jogador == 1:
        print('\033[1;33mVoce PERDEU!!!\033[0m')
    elif jogador == 2:
        print('\033[7;34mEmpate!\033[0m')
    else:
        print('\033[7;31mERRO\033[1;31mJogada invalida!\033[0m')


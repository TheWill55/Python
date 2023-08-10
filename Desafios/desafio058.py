from random import randint
pc = randint(0,10)
print('Vamos jogar? \nTente adivinhar qual número eu escolhi!')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite seu palpite, qual sera o número que escolhi?'))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais.... Tente novamente!')
        else:
            print('Menos... Tente novamente!')
print('Parabens você acertou, {} Tentativas!'.format(palpites))

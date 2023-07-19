import random
computador = random.randint(0,5)
adv = int(input('Tente adivinhar o numero que o computador gerou:'))
import time
print('Processando...')
time.sleep(3)
if computador == adv:
    print('Você acertou! {} foi o numero escolhido pela maquina!'.format(computador))
else:
    print('Você perdeu! {} foi o numero escolhido pela maquina!'.format(computador))
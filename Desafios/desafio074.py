from random import randint

num1 = (randint(1,99), randint (1,99), randint(1,99), randint(1,99), randint(1,99))
print('Os números sortiados são :')
for n in num1:
    print(f'{n} ', end='')
print(f'\nO maior valor foi {max(num1)}')
print(f'O menor valor foi {min(num1)}')

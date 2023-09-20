"""
num = [5,9,7,2]
num[3] = 8
num.append(7)
num.sort(reverse=True)
num.insert(2,2)
if 7 in num:
	num.remove(7)
else:
	print('Não existe!')
print(num)
print(f"Essa lista tem {len(num)} elementos.")

"""

"""
valores = []
for cont in range(1,10):
	valores.append(int(input('Digite valores: ')))
for c,  valor in enumerate(valores):
	print(f'Na posição {c} encontrei o valor {valor}!')
print('Final de teste!')

"""
from random import randint
a = [2,1,5,3]
b = a[:]

b[3] = randint(6,20)

print(f'Lista A: {a} ')
print(f'Lista B: {b}')
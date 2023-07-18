num = int(input('Digite um numero:'))
print('Analizando o número digitado: {}'.format(num))
uni = num // 1 % 10
des = num // 10 % 10 
cent = num // 100 % 10
mil = num // 1000 % 10
print('Unidade: {}'.format(uni))
print('Dezena: {}'.format(des))
print('Centena: {}'.format(cent))
print('Milhar: {}'.format(mil))

num = (int(input('Digite um número: ')),
       int(input('Digite o segundo número: ')),
       int(input('Digite o terceiro número: ')),
       int(input('Digite o quarto número: ')))


print(f'Você digitou os seguintes valores {num}')
if 9 in num:
	print(f'O número 9 apareceu {num.count(9)} vezes!')
else:
	print('O número 9 não apareceu nenhuma vez!')
if 3 in num:
	print(f'O valor 3 apareceu na {num.index(3)+1} posição!')
else:
	print('O valor 3 não foi digitado em nenhuma posição!')
for n in num:
	if n % 2 == 0:
		print(n)
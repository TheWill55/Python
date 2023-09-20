num = list()
while True:
	n = int(input('Digite um valor: '))
	if n not in num:
		num.append(n)
	else:
		print('Valor duplicado! Erro ao adicionar...')
	r = str(input('Gostaria de cuntiunuar? S/N: '))
	if r in 'Nn':
		break
print('-' * 50)
num.sort()
print(f'Você digitou os valores{num}')

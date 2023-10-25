num = [[],[]]
valor = 0
for c in range(7):
	valor = int(input(f'Digite o {c} valor: '))
	if valor % 2 ==0:
		num[0].append(valor)
	else:
		num[1].append(valor)
num[0].sort()
num[1].sort()
print(f'Os números inpares foram {num[1]}')
print(f'Os números pares foram {num[0]}')
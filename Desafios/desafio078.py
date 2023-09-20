listidade = []
maior = 0
menor = 0
for contador in range (0,6):
	listidade.append(int(input(f'{contador} - Digite a idade:  ')))
	if contador == 0:
		maior = menor = listidade[contador]
	else:
		if listidade[contador] > maior:
			maior = listidade[contador]
		if listidade[contador] < menor:
			menor = listidade[contador]
print('$' * 50)
print(f'As seguintes idades {listidade} foram guardadas com sesgurança!')
print(f'A maior idade é {maior} que esta na posição ', end='')
for i , v in enumerate(listidade):
	if v == maior:
		print(f'{i}...!', end='')
print(f'A menor idade é {menor} que esta na posição ', end='')
for i, v in enumerate(listidade):
	if v == menor:
		print(f'{i}...!', end='')


temp= []
princ = []
mai = men = 0
while True:
	temp.append(str(input('Digite o nome: ')))
	temp.append(float(input('Digite o peso: ')))
	if len(princ) == 0:
		mai = men = temp[1]
	else:
		if temp[1] > mai:
			mai = temp[1]
		if temp[1] < men:
			men = temp[1]
	princ.append(temp[:])
	temp.clear()
	continua = str(input('Gostaria de continuar? S/N ')).strip().upper()
	if continua in "N":
		break
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O maior pesso foi de {mai}Kg',end=" ")
for p in princ:
	if p[1] == mai:
		print(f'{p[0]}',end=" ")
print(f'O menor peso foi de {men}Kg ', end=" ")
for pe in princ:
	if pe[1] == men:
		print(f'{pe[0]}',)
print('Fim de progama!')

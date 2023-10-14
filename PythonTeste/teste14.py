"""
teste = []
teste.append('Wilson')
teste.append(23)
galera = []
galera.append(teste[:])
teste[0] = 'Victor'
teste[1] = 20
galera.append(teste[:])
print(galera)

galera = [['Wilson', 23], ['Leonardo', 20], ['João', 52], ['George', 19]]
for pessoa in galera:
	print(f'Nome: {pessoa[0]}, {pessoa[1]} anos.')
"""

galera = list()
dado = list()
totalmaior = totalmenor = 0

for contador in range(0,5):
	dado.append(str(input('Digite o nome: ')))
	dado.append(int(input('Idade: ')))
	galera.append(dado[:])
	dado.clear()
for pessoa in galera:
	if pessoa[1] >=18:
		print(f'{pessoa[0]} é maior de idade')
		totalmaior +=1
	else:
		print(f'{pessoa[0]} é menor de idade')
		totalmenor +=1
print(f'Temos {totalmaior} maiores de idade e temos {totalmenor} menores de idade')

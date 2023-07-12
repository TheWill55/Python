from random import shuffle
pe1 = str(input('Primeiro nome:'))
pe2 = str(input('Segundo nome:'))
pe3 = str(input('Terceiro nome:'))
pe4 = str(input('Quarto nome:'))
pe5 = str(input('Quinto nome:'))
lista = [pe1,pe2,pe3,pe4,pe5]
shuffle(lista)
print('A sequencia é')
print(lista)
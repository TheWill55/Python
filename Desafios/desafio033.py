va1 = int(input('Digite o primeiro valor:'))
va2 = int(input('Digite o segundo valor:'))
va3 = int(input('Digite o terceiro valor'))
menor = va1
if va2 < va1 and va2 < va3:
    menor = va2
if va3 < va1 and va3 < va2:
    menor = va3
print('O menor valor digitado foi {}'.format(menor))
maior = va3
if va1 > va2 and va1 > va3:
    maior = va1
if va2 > va1 and va2 > va3:
    maior = va2
print('O maior numero digitado foi {}'.format(maior))
soma = 0
cont = 0
for nu in range(1, 7):
    num = int(input('({}): número: '.format(nu)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))

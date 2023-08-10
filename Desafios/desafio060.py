nu = int(input('Digite um número para ver seu fatorial: '))
cont = nu
fac = 1
while cont > 0:
    print('{}'.format(cont),end=' ')
    print('x ' if cont > 1 else '= ',end='' )
    fac = fac * cont
    cont -= 1
print('{}'.format(fac))
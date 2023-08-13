print('| Sequência de Fibonacci |')
termos = int(input('Quantos termos você quer mostrar?'))
t1 = 0
t2 = 1
print('{} > {}'.format(t1,t2), end='')
cont = 3
while cont <= termos:
    t3 = t1 + t2
    print(' > {}'.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' > Fim!')



numero = int(input('Digite o termo para mostrar a sequencia da Fibo: '))
t5 = 0
t6 = 1
cont2 = 3
while cont <= numero:
    t7 = t5 + t6
    t5 = t6
    t6 = t7
    cont2 = cont2 + 1
print('Fim!')
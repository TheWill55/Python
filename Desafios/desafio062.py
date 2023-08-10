print('Gerando PA!')
print('\033[1;32m-\033[0m' * 20 )
termo2 = int(input('Digite o primeiro termo: '))
razao2 = int(input('Razão da PA: '))
termo = termo2
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('\033[1;34m |{}| \033[0m'.format(termo), end='')
        termo += razao2
        cont = cont + 1
    print('PAUSA!')
    mais = int(input('Quantos termos você gostaria de mostrar a mais? '))
print('Total de termos mostrado {}!'.format(total))
print('Exercício completo!')

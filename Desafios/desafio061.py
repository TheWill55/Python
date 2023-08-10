print('Gerador de PA!')
print('=' * 20)
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = termo1
cont = 1
while cont <= 10:
    print(' <{}> '.format(termo), end='')
    termo += razao
    cont = cont + 1
print('Fim!')

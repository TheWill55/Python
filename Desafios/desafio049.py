numero = int(input('Digite um numero para ver sua tabuada!: '))
for tab in range(1, 11):
    print('{} X {:2} = {}'.format(numero, tab , numero * tab))

print('=======Dinheiro Acumulado:=======')
di = float(input('Dinheiro em conta:'))
print('Dinheiro sem rendimento: R${}'.format(di))
if di >= 29000:
    btc = 29000
    to1 = di / 100
    print('Total em BTC acumuldado {}'.format(to1))
elif di >= 2.8:
    xrp = 2.8
    to2 = di / 2.8
    print('Total acumulado em XRP {}'.format(to2))
else:
    print('Impossivel de Investir !')

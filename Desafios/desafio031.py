km = float(input('Digite a distancia:'))
print('A distancia da viagem é de {:.0f}KM'.format(km))

if km <= 200:
    pas = 0.50 * km
    print('Total a ser pago R${}'.format(pas))
else:
    des = 0.45 * km
    print('Valor a ser pago com desconto é R${}'.format(des))
print('Boa viagem!')
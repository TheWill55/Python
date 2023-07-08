dia = int(input('Dias percorrido com o carro:'))
km = float(input('Quantos KM percorrido?'))
val = (dia * 60) + (km * 0)
print('O total a pagar é de R${:.2F}'.format(val))
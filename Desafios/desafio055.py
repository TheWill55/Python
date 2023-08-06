maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Digite o pesso -> {}= pessoa: '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('{}Kg é  o Maior Peso!'.format(maior))
print('{}Kg é o Menor Peso!'.format(menor))


pes = float(input('Digite seu peso: KG'))
alt = float(input('Digite sua altura: m'))
imc = pes / (alt ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('IMC abaixo de 18.5: abaixo do Peso!')
elif imc < 25:
    print('IMC ideal! ')
elif imc < 30:
    print('Melhor se cuidar mais! IMC SOBREPESO!')
elif imc < 40:
    print('Melhor parar de comer po**a! IMC OBESIDADE')
else:
    print('Proucure um médico imediatamente! IMC OBESIDADE MÓRBIDA')
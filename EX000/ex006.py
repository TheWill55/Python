num1 = int(input('Digite um valor:'))
num2 = int(input('Digite outro valor:'))
soma = num1 + num2
mult = num1 * num2 
sub = num1 - num2
div = num1 / num2
dint = num1 // num2
espo = num1 ** num2 
print('A soma é {}, a multiplicação é {}, a divisão é {}.'.format(soma,mult,div))
print('Divisão inteira {} e potência {:.3f}.'.format(dint,espo))
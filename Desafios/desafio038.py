num1 = int(input('Digite o primeiro numero:'))
num2 = int(input('Digite outro numero:'))
if num1 > num2:
    print('O primeiro valor \033[1;32m{}\033[0m é maior que o segundo valor \033[1;31m{}\033[0m!'.format(num1, num2))
elif num2 > num1:
    print('O segundo valor: \033[1;31m{}\033[0m é maior que o primeiro valor: \033[1;32m{}\033[0m'.format(num2, num1))
else:
    print('\033[1;33mNúmeros iguais!\033[0m')
    
num = int(input('Digite um número inteiro: '))
print(''' Escolha uma das seguintes opções para converter :
      [1] Converter número para Binário
      [2] Converter número para Actal
      [3] Converter número para Hexadecimal''' )
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para ACTAL é igual a {}'.format(num,oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else: 
    print('Por favor tente novamente!')
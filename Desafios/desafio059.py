from time import sleep
valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('Escolha uma das opções para ver um resultado!')
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do progama''')
    opcao = int(input('Qual opção desejada? '))
    if opcao == 1:
        soma = valor1 + valor2
        print('Soma entre {} e {} é {}!'.format(valor1,valor2,soma))
    elif opcao == 2:
        mult= valor1 * valor2
        print('Multiplicando {} com {} o resultado é {}!'.format(valor1,valor2,mult))
    elif opcao == 3:
        if valor1 > valor2:
            print('O primeiro valor é o MAIOR!')
        else:
            print('O segundo valor é MAIOR')
    elif opcao == 4:
        print('Informe os números novamente!')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
        print('')
    elif opcao == 5:
        print('Finalizando...')
        
    else:
        print('Opção invalida!')
    sleep(1)
print('Fim do Programa!')

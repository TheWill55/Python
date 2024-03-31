def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: POR FAVOR DIGITE UM NUMERO INTEIRO VALIDO.')
            continue
        except KeyboardInterrupt:
            print('Entrada de dados interrompida pelo usuario.')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO NA ENTRAA DE DADO, POR FAVOR DIGITE UM NUMERO RELA')
        except KeyboardInterrupt:
            print('DADOS NAO GIGITADOS PELO USUARIO')
            return 0
        else:
            return n
            
 
num1 = leiaInt('Digite um numero interio: ')
num2 = leiaFloat('Digite um numero real: ')
print(f'O valor inteiros digitado foi {num1} e o real foi {num2}')

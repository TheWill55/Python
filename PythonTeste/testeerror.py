try: 
    a = int(input('Digite um valor: '))
    b = int(input('Digite outro valor '))
    r = a / b
    
except (ValueError, TypeError):
    print('Tivemos um problema com os tiopos de  dados que voce digitou!')
except ZeroDivisionError:
    print(' Nao e possivel divir um numero pro zero! ')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados')
except Exception as erro:
    print('Infelismete tivemos um ERRO :( {erro.__cause__}')
else:
    print(f'Voce digitou {r}')
finally:
    print(' Volte sempre! Muito obrigado! ')
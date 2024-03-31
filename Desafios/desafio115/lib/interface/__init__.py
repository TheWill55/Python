def leiaInt(msg):
    try:
        n = int(input(msg))
    except (ValueError, TypeError):
        print('ERRO: por favor, digite um numero inteiro valido!')
    except(KeyboardInterrupt):
        print('Usuario preferiu nao digitar esse numero!')
        return 0
    else:
        return n
        
def linha(tam = 42):
    return '-' * tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())
    
def menu(lista):
    cabecalho(' MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opcao: ')
    return opc
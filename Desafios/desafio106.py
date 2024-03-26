from colorama import Fore, Back, Style, init

init(autoreset=True)

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', Fore.GREEN)
    print(Back.WHITE, end='')
    help(com)

def titulo(msg, cor=Fore.RESET):
    tam = len(msg) + 4
    print(cor + '=' * tam)
    print(f'  {msg}  ')
    print('=' * tam)
    print(Style.RESET_ALL, end='')

comando = ' '
titulo('Sistema de Ajuda Python help', Fore.RED)
while True:
    comando = input('Funcao ou Biblioteca > ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('FIM!', Fore.RED)

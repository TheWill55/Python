from datetime import date
pres = date.today().year
nome = str(input('Digite seu nome: '))
ano = int(input('Digite o ano de nascimento: '))
ida = pres - ano
if ida <= 9:
    print('Atleta {}, com {} anos tem a categoria: \033[1;33m Mirim. \033[0m'.format(nome, ida))
elif ida >= 9 and ida < 14:
    print('Atleta {}, com {} anos tem a categoria: \033[1;32m Infantil. \033[0m'.format(nome, ida))
elif ida >= 14 and ida < 19:
    print('Atleta {}, com {} anos tem a categoria: \033[1;31m Junior. \033[0m'.format(nome, ida))
elif ida >= 19 and ida < 25:
    print('Atleta {}, com {} anos tem a categoria: \033[1;34m Senior. \033[0m'.format(nome, ida))
else:
    print('Atleta {}, com {} anos tem a categoria: \033[1;35m Master. \033[0m'.format(nome, ida))
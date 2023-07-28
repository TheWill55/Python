from datetime import date
atual = date.today().year
ano = int(input('Digite o ano em que você nasceu:'))
idade = atual - ano
print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))
if idade == 18:
    print('Alistamento obrigatório nesse ano atual!')
elif idade < 18:
    fal = 18 - idade
    print('Alistamento ainda não nescessario ainda, faltam apenas {} anos !'.format(fal))
elif idade > 18:
    fal2 = idade - 18 
    print('Você ja deveria ser se alistados a {} anos!'.format(fal2))


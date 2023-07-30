nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2 
print('O aluno teve uma media de {:.1f} com os calculos de suas nota!'.format(media))
if media >= 7.0:
    print('Você foi aprovado no vestibular!')
elif media >=5 and media <7:
    print('Você ficou de reculperação!')
elif media < 5.0:
    print('Você foi reprovado!')

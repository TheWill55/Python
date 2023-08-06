somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('=====Pessoa {}.====='.format(p))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digte a Idade: '))
    sexo = str(input('Sexo: [M] ou [F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo  in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A media de idade das pessoas é {:.0f}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}!'.format(maioridadehomen, nomevelho))
print('À apenas {} pessoa(s) com a idade abaixo dos 20 anos!'.format(totmulher20))
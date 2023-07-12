import random
aluno1 = str(input('Primeiro Aluno:'))
aluno2 = str(input('Segundo Aluno:'))
aluno3 = str(input('Terceiro Aluno:'))
aluno4 = str(input('Quarto Aluno:'))
aluno5 = str(input('Quinto Aluno:'))
lista = [aluno1,aluno2,aluno3,aluno4,aluno5]
prem = random.choice(lista)
print('O aluno premiado foi {}'.format(prem))
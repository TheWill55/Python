sal = float(input('Salari do funcionario: R$'))
if sal <= 1250.55:
    alm = sal + (sal * 15 / 100)
else:
    alm = sal + (sal * 10 /100)
print('Quem ganhava R${:.2f} , passará a ganhar R${:.2f} por mês! '.format(sal,alm))
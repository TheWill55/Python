sal= float(input('Salário do seu trabalho:'))
mes = 12
total = sal*mes
print('Ganho anual com trabalho fixo foi de {}'.format(total))
ext = float(input('Renda extra:'))
mes2 = 12
total2 = ext*mes2
print('Sua renda extra anual foi de {}'.format(total2))
prog = float(input('Ganhos com desenvolvimentos:'))
mes3 = 12
total3 = prog * mes3
print('Total acumulado anual é de {}!'.format(total3))
soma = total + total2 + total3
print('Seu ganho anual foi de {} Reais, resultado do calculo do seu salário, com sua renda extra e seu trabalho de desenvolvimento '.format(soma))
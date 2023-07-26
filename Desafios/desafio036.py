casa = float(input('Valor da casa:'))
sal = float((input('Salário do comprador:')))
ano = int(input('Quantidade de parcelas por ano:'))
mes = casa / (ano * 12)
print('Para pagar uma casa no valor de \033[1;33mR${:.2f}\033[0m em {} anos, suas prestações estarão no valor de \033[1;33mR${:.2f}\033[0m'.format(casa,ano,mes))
ma = sal * 30 / 100
if mes <= ma :
    print('O emprestimo foi \033[1;32m APROVADO \033[0m !')
else:
    print('Emprestivo \033[1;31m NEGADO \033[0m !')
    
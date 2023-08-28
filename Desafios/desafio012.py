print('Desconto')
prod = float(input('Qual o valor do produto?'))
desc = prod - (prod * 10/100)
print('O valor do produto é R${:.2f} , com o desconto 10%, o valor final fica: R${:.2f} !'.format(prod,desc))


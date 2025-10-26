print('Desconto')
prod = float(input('Qual o valor do produto?'))
desc = prod - (prod * 10/100)
print(f'O valor do produto é R${prod:.2f} , com o desconto 10%, o valor final fica: R${desc:.2f} !')



pro = float(input('Digite o valor: R$'))
print('''Tipo de pagamento
      [1] À vista dinheiro/PIX
      [2] À vista cartão
      [3] 2x no cartão
      [4] 3x ou mais no cartão''' )
opcao = int(input('Qual a opcão escolhida? '))
if opcao == 1:
    desc = pro - (pro * 10 / 100)
    print('Pagamento a vista dinheiro ou PIX!')
    print('Valor do Produto ==== R$ {:.2f} \n Total a pagar com DESCONTO DE 10% : \033[1;32mR$ {:.2f}\033[0m'.format(pro,desc))
elif opcao == 2:
    desc = pro - (pro * 5 / 100)
    print('À vista no cartão')
    print('Valor do produto ==== R$ {:.2f} \n Total a pagar com DESCONTO DE 5% : \033[1;32mR$ {:.2f}\033[0m'.format(pro,desc))
elif opcao == 3:
    parce = pro / 2
    print('2x no cartão')
    print('Valor do produto ==== R$ {:.2f} \n Em 2x de : \033[1;32mR$ {:.2f}\033[0m'.format(pro,parce))
elif opcao == 4:
    total = pro + (pro * 20 / 100)
    nuparc = int(input('Quantas vezes você deseja parcelar sua compra? :'))
    parce = total / nuparc
    print('Valor total do produto com TAXA : R$ {:.2f} \n Parcelas de {}X de R${:.2f}'.format(total,nuparc,parce))
else:
    opcao = 0
    print('Volte ao inicio para ver as opcões de pagamento!')
    




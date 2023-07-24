print('===Aparelho: Xiaomi mi 13===')
print('   Valor: R$ 1846.54 ')
din = float(input('Dinheiro na conta:'))
cell = 1846.54
print('Dinehiro em conta é R$\033[1;32m{:.2f}\033[m'.format(din))
if din >= cell:
    print('Compra altorizada!')
    sob = din - cell
    print('Total restante em conta é R${:.2f}'.format(sob))
else:
    print('Compra negada!')
    falta = cell - din
    print('Falta apenas R${:.2f} para a compra do aparelho'.format(falta))
print('Agradeçemos, volte sempre!')


id = 19 // 2 , 19%2
print(id)
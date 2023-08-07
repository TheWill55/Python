print('-' * 20)
print('  Gestão de Banca  ')
print('-' * 20)
valorinicial = float(input('Digite o valor inicial da banca: $'))
print('Meta Diaria: \033[1;32m12.5%\033[0m \nMeta de ganho: $5000.00')
print('Limite de perca: -10%')
stop = valorinicial - (valorinicial * 10 / 100)
print('Stop da Banca: \033[1;31m${:.2f}\033[0m'.format(stop))
print('~' * 50)
meta = 0
diasmetas = 0
print('| Dias | Projeção | Lucro |')
for dia in range(1,31):
    meta = valorinicial * 12.5 / 100
    diasmetas = meta + valorinicial
    valorinicial = diasmetas
    print('{:^7} {:^11.2f} {:^8.2f}'.format(dia, diasmetas, meta))
print('Você ficara com a banca positiva no final se seguir esse gerenciamento')
lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.90,
         'Estojo', 25,
         'Transferidor', 4.20,
         'Mochila', 120.32,
         'Canetas', 22.32,
         'Livro', 34.90)

print('-' * 30)
for item in range(0, len(lista), 2):
    nome = lista[item]
    preco = lista[item + 1]
    print(f'{nome:.<20} R${preco:>7.2f}')
print('-' * 30)


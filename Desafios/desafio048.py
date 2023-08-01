soma = 0
cont = 0 
for impa in range(1, 500, 2):
    if impa % 3 == 0:
        cont = cont + 1
        soma = soma + impa
print('A soma de todos os {} números solicitado é {}'.format(cont,soma))

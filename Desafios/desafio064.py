numero = 1
cont = soma = 0
numero = int(input('Digite um numero [0 para sair!]'))
while numero != 0:
    soma += numero
    cont = cont + 1
    numero = int(input('Digite um numero [0 para sair!]'))
print('Total de números digitados: {}, somando eles o resultado é {}'.format(cont, soma))
print('Fim!')
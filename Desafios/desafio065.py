resposta = 'S'
soma = quant = media = maior = menor = 0
while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
media = soma / quant
print('Total de números digitados: {} \nA media entre os números digitados é {:.1f}'.format(quant,media))
print('O maior número digitado foi {} e o menor número digitado foi {}'.format(maior,menor))
print('Fim!')

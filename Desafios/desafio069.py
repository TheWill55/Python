tot18 = totm = totf = 0
while True:
    idade = int(input('Digite a Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totm += 1
    if sexo == 'F' and idade < 20:
            totf += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str('Deseja continuar? [S/N] ').strip().upper()[0]
    if resposta == 'N':
        break
print(f'Total de pessoal mair de 18 anos: {tot18}')
print(f'Total de Homens cadastrados são: {totm}')
print(f'Totais de Mulheres com a idade abaixo dos 20 anos: {totf}')
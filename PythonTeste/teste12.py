nu = soma = 0
while True:
    nu = int(input('Digite um número: '))
    if nu == 5:
        break
    soma += nu
print(f'A soma é {soma}')
cont = soma = 0
while True:
    num = int(input('Digite um número  (999 para parar!): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Ao todo você digitou {cont} e a soma de todos eles da {soma}!')

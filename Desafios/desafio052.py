num = int(input('Digite um numero:'))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')
        total = total + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n \033[0m O número {} foi divisível {} vezes!'.format(num, total))
if total ==2:
    print('O número digitado é primo!')
else:
    print('O número digitado não é primo')
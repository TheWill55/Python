while True:
    nu = int(input('Quer ver a tabuada de qual número ? '))
    if nu < 0:
        break
    for c in range(1, 11):
        print(f'{nu} x {c} = {nu*c}')
print('Fim!')

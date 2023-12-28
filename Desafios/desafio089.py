ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media  = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp =str(input('Gostaria de continuar? s/n ')).upper()
    if resp in 'N':
        break
print('+' * 50)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('+' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas de qual aluno? (999 interromper)'))
    if opc === 999:
        print('Finalizado')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]} ')
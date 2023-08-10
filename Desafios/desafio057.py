sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Informação invalida, informe novamente o sexo: ')).strip().upper()[0]
print('Fim! O sexo {} foi registrado com sucesso!'.format(sexo))

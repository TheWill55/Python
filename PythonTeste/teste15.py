"""
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
estado3 = { 'uf':'Santa Catarina', 'sigla':'SC'}

brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)
print(brasil[2] ['uf'])
"""

estado = dict()
brasil = dict()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: ')).upper()
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
        
"""print('-' * 20)
print('  Gestão de Banca  ')
print('-' * 20)
valorinicial = float(input('Digite o valor inicial da banca: $'))
print('Meta Diaria: \033[1;32m12.5%\033[0m \nMeta de ganho: $5000.00')
print('Limite de perca: -10%')
stop = valorinicial - (valorinicial * 10 / 100)
print('Stop da Banca: \033[1;31m${:.2f}\033[0m'.format(stop))
print('~' * 50)
meta = 0
diasmetas = 0
print('| Dias | Projeção | Lucro |')
for dia in range(1,31):
    meta = valorinicial * 12.5 / 100
    diasmetas = meta + valorinicial
    valorinicial = diasmetas
    print('{:^7} {:^11.2f} {:^8.2f}'.format(dia, diasmetas, meta))
print('Você ficara com a banca positiva no final se seguir esse gerenciamento')

# Imprime o cabeçalho
print('-' * 20)
print('  Gestão de Banca  ')
print('-' * 20)

# Solicita o valor inicial da banca ao usuário
valorinicial = float(input('Digite o valor inicial da banca: $'))

# Imprime metas e limites
print('Meta Diária: \033[1;32m12.5%\033[0m \nMeta de ganho: $5000.00')
print('Limite de perda: -10%')

# Calcula o valor do stop da banca
stop = valorinicial - (valorinicial * 10 / 100)
print('Stop da Banca: \033[1;31m${:.2f}\033[0m'.format(stop))
print('~' * 50)

# Inicializa variáveis
meta_diaria_percentual = 12.5
diasmetas = valorinicial

# Imprime cabeçalhos da tabela
print('| Dias | Projeção | Meta Diária |')

# Loop para 30 dias
for dia in range(1, 31):
    # Calcula a meta diária e a projeção da banca
    meta_diaria = diasmetas * (meta_diaria_percentual / 100)
    diasmetas += meta_diaria
    
    # Imprime os resultados formatados
    print('{:^7} {:^11.2f} {:^12.2f}'.format(dia, diasmetas, meta_diaria))

# Imprime uma mensagem final
print('Você ficará com a banca positiva no final se seguir esse gerenciamento')

"""


def calcular_projecao_banca(valor_inicial, meta_percentual, dias):
    banca = valor_inicial
    for dia in range(1, dias + 1):
        meta_diaria = banca * (meta_percentual / 100)
        banca += meta_diaria
    return banca

taxa_de_cambio = 6.19

print('-' * 20)
print(f"Gestão de Banca")
print('-' * 20)

valor_inicial = float(input(f"Digite o valor inicial da banca em EURO: $ "))

periodo = int(input(f"Escolha o período (30 ou 60 dias): "))

escolha_moeda = input('Escolha a moeda de exibição (Digite "D" para dolar ou "R" para reais): ').upper()

stop = valor_inicial - (valor_inicial * 8 / 100)
print('Stop da Banca: \033[1;31m${:.2f}\033[0m'.format(stop))
print('_' * 56)

meta_diaria_percentual = 8.1
diasmetas = valor_inicial

print('{:^15}{:^20}{:^20} '.format("Dias", "|    Projeção    |", "Meta Diária"))
print("_" * 56)

for dia in range(1, periodo + 1):
    meta_diaria = diasmetas * (meta_diaria_percentual / 100)
    diasmetas += meta_diaria
    
    print('{:^15} {:^20.2f} {:^20.2f}'.format(dia, diasmetas, meta_diaria))
print("_" * 56)
if escolha_moeda == 'R':
    diasmetas_reais = diasmetas * taxa_de_cambio
    print('Projeção da Banca em Reais após {} dias: R$ {:.2f}'.format(periodo, diasmetas_reais))
else:
    print('Projeção da Banca em DOLAR após {} dias: $ {:.2f}'.format(periodo, diasmetas))
    
print('Você ficará com a banca positiva no final se seguir esse gerenciamento')
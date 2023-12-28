# Declaração das variáveis
nome_criptoativo = ""
valor_data_compra = 0.0
data_compra = ""
quantidade = 0.0

# Leitura dos dados
nome_criptoativo = input("Digite o nome do criptoativo: ")
valor_data_compra = float(input("Digite o valor da data da compra: "))
data_compra = input("Digite a data da compra (DD/MM/AAAA): ")
quantidade = float(input("Digite a quantidade: "))

# Cálculo do valor total da aquisição
valor_total_aquisicao = valor_data_compra * quantidade

# Impressão da tabela
print("| Nome do criptoativo | Valor da data da compra | Data da compra | Quantidade | Valor total da aquisição |")
print("|---|---|---|---|---|")
print(f"| {nome_criptoativo} | {valor_data_compra} | {data_compra} | {quantidade} | {valor_total_aquisicao} |")
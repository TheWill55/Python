def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31m ERRO: \"{entrada}\" e um preco invalido! \033[0m')
        else:
            valido = True
            return float(entrada)
                
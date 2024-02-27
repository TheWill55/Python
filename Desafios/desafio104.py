def leiaInt(mensagem):
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada
        except ValueError:
            print("Por favor, Digite um valor numérico válido!")
n = leiaInt('Digite um número inteiro: ')
print("Você digitou: ", n)
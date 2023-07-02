# Definição da classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")

# Criando um objeto Pessoa
pessoa1 = Pessoa("João", 25)

# Chamando o método cumprimentar do objeto pessoa1
pessoa1.cumprimentar()
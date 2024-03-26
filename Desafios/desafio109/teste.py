import moeda

p = float(input("Digite um preco: R$ "))
print(f"A metade de {moeda.moeda(p)} e {(moeda.metade(p, True))}")
print(f"O dobro de {moeda.moeda(p)} e {(moeda.dobro(p, True))}")
print(f"Aumentando 10%, teremos o valor de {(moeda.aumentar(p, 10, True))}")
print(f"Diminuindo 10%, teremos o valor de {(moeda.diminuir(p, 10, True))}")
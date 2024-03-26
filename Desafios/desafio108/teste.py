import moeda

p = float(input("Digite um preco: R$ "))
print(f"A metade de {moeda.moeda(p)} e {moeda.moeda(moeda.metade(p))}")
print(f"O dobro de {moeda.moeda(p)} e {moeda.moeda(moeda.dobro(p))}")
print(f"Aumentando 10%, teremos o valor de {moeda.moeda(moeda.aumentar(p, 10))}")
print(f"Diminuindo 10%, teremos o valor de {moeda.moeda(moeda.diminuir(p, 10))}")
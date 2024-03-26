import moeda

p = float(input("Digite um preco: R$ "))
print(f"A metade de R${p} e R${moeda.metade(p)}")
print(f"O dobro de R${p} e R${moeda.dobro(p)}")
print(f"Aumentando 10%, teremos o valor de R${moeda.aumentar(p, 10)}")
print(f"Diminuindo 10%, teremos o valor de R${moeda.diminuir(p, 10)}")
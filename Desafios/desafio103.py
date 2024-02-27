def ficha(nome, gols):
    if nome is None:
        nome = "Jogador desconhecido"
    if gols is None:
        gols = 0
    return "Nome: " + nome + ", Gols: " + str(gols)

nome_jogador = input("Digite o nome do jogador(Opcional): ")
gols_jogador = input(f"Digite a quantidade de gols do {nome_jogador}: ")

if nome_jogador == "" and gols_jogador == "":
    print(ficha(None,None))
elif nome_jogador == "":
    print(ficha(None, int(gols_jogador)))
elif gols_jogador == "":
    print(ficha(nome_jogador, None))
else:
    print(ficha(nome_jogador, int(gols_jogador)))
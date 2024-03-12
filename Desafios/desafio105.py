"""
def notas(notas):
    if notas is None:
        return {}

    maior_Nota = notas[0]
    menor_Nota = notas[0]
    soma_Notas = 0
    quantidade = 0

    for nota in notas:
        if nota > maior_Nota:
            maior_Nota = nota
        if nota < menor_Nota:
            menor_Nota = soma_Notas + nota
        quantidade = quantidade + 1

    media = soma_Notas / quantidade


    def criar_dicionario_com_situacao(situacao):
        return{
            "quantidade": quantidade,
            "maiorNota": maior_Nota,
            "menorNota": menor_Nota,
            "media": media,
            "situacao": situacao
        }
    
    if "situacao" in locals():
        return criar_dicionario_com_situacao(situacao)
    else:
        return {
            "qauntidade": quantidade,
            "maiorNota" : maior_Nota,
            "menorNota" : menor_Nota,
            "media" : media
        }

notas_alunos = [8, 5, 4, 8, 9]
resultado = notas(notas_alunos)
print(resultado)

"""
def notas(notas, situacao=None):
    if not notas:
        return {}  # Retorna um dicionário vazio se a lista de notas estiver vazia
    
    maior_nota = max(notas)
    menor_nota = min(notas)
    soma_notas = sum(notas)
    quantidade = len(notas)
    media = soma_notas / quantidade
    
    if situacao:
        return {
            "quantidade": quantidade,
            "maiorNota": maior_nota,
            "menorNota": menor_nota,
            "média": media,
            "situação": situacao
        }
    else:
        return {
            "quantidade": quantidade,
            "maiorNota": maior_nota,
            "menorNota": menor_nota,
            "média": media
        }

# Exemplo de uso:
notas_alunos = [8, 7, 6, 9, 8]
resultado = notas(notas_alunos, situacao="Aprovado")
print(resultado)

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
def notas(notas, situacao=False):
    h = dict()
    h['Quantidade'] = len(notas)
    h['Maior nota'] = max(notas)
    h['Menor nota'] = min(notas)
    h['Media'] = sum(notas)/len(notas)
    if situacao:
        if h['Media'] >= 8:
            h['sitacao'] = 'TOP'
        elif h['Media'] == 7:
            h['sitacao'] = 'Estude mais'
        else:
            h['sitacao'] = 'REPROVADO'
    return h
   

notas_alunos = [6 ,8, 10, 6, 5]
resultado = notas(notas_alunos, situacao = True )
print(resultado)

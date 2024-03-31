from desafio115.lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
    
def criarArquivo(nome):
    try:
        a = open(nome, 'wb+')
        a.close()
    except Exception as e:
        print(f'Houve um ERRO ao criar o arquivo: {e}')
    
    else:
        print(f'Arquivo  {nome} criardo com sucesso!')
'''
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao tentar ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        print(a.readlines())
'''

def lerArquivo(nome):
    try:
        with open(nome, 'rt') as a:
            cabecalho('PESSOAS CADASTRADAS')
            for linha in a:
                dado = linha.split(';')
                # Usando .strip() para remover possíveis espaços em branco e caracteres de nova linha
                dado[1] = dado[1].replace('\n', '')
                print(f'{dado[0]:<30}{dado[1]:>3} anos')
    except Exception as e:  # Capturando a exceção para possivelmente imprimir um  erro mais específico
        print(f'ERRO ao tentar ler o arquivo: {e}')
    finally:
        a.close()
        

def cadastrar(arq, nome = 'desconehcido', idade = 0 ):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve eum ERRO na hora de escrever os dados! ')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
    


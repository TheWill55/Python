import sys
sys.path.append('C:/Users/Wilson Alves/Documents/GitHub/Python/Desafios')

from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep
import os


diretorio = 'C:/Users/Wilson Alves/Documents/GitHub/Python/Desafios/desafio115'
arq = os.path.join('C:/Users/Wilson Alves/Documents/GitHub/Python/Desafios/desafio115', 'cursoemvideo.txt')
caminho_completo = os.path.join(diretorio, arq)

if not arquivoExiste(caminho_completo):
    criarArquivo(caminho_completo)

while True:
    resposta = menu(['Ver pressoas cadastradas ','Cadastrar nova Pessoa','Sair do Sistema'])
    if resposta == 1:
        # opcao de listar o conteudo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #opcao de cadastrar nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema!... ')
        break
    else:
        cabecalho('ERRO, digite uma opcao valida!')
    sleep(2)


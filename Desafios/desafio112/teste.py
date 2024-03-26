import sys
sys.path.append('C:/Users/Wilson Alves/Documents/GitHub/Python/Desafios')

from desafio111.utilidadescev.moeda import resumo
from desafio112.utilidadescev import dado



p = dado.leiaDinheiro('Digite o valor: R$')
resumo(p, 20, 12)



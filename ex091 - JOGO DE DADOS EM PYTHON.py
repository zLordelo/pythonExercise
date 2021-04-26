from random import randint
from time import sleep
from operator import itemgetter #MODULO SERVE PARA PEGAR O ITEM EM UM DICIONÁRIO
print('=' * 50)
print(f'\033[1;31m{"JOGO DE DADOS EM PYTHON":^50}\033[m')
print('=' * 50)
'''Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e 
tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
jogador = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
ranking = list()

for k, v in jogador.items():
    print(f'O \033[1m{k}\033[m tirou \033[1m{v}\033[m no dado.')
    sleep(1)

print('=' * 50)
print(f'\033[1;33m{"RANKING DOS VENCEDORES":^50}\033[m')
print('=' * 50)
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º LUGAR: {v[0]} com {v[1]}.'.center(50))
    sleep(0.5)
print('=' * 50)
print(f'\033[1;31m{"FICHA DO JOGADOR":^50}\033[m')
print('=' * 50)
'''Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''


def ficha(nome= '<desconhecido>', gols=0):
    if type(gols) == str:
        gols = 0
    else:
        gols = gols
    print(f'O jogador {nome} fez {gols} gols nessa partida.')


n = str(input('Nome do jogador: ')).strip().capitalize()
g = str(input(f'Quantos gols fez: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n, g)
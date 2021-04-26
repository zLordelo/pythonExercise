from random import randint
from time import sleep
print('=' * 50)
print(f'\033[1;31m{"PALPITES PARA A MEGA SENA":^50}\033[m')
print('=' * 50)
'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA 
a criar palpites.O programa vai perguntar quantos jogos serão gerados e 
vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
megasena = list()
jogo = list()
quant = int(input('Quantos jogos serão gerados: '))
cont = 0
print()
print('=' * 10, f'SORTEANDO {quant} JOGOS', '=' * 10)
while cont != quant:
    for c in range(1, 7):
        jogo.append(randint(1, 60))
    jogo.sort()
    megasena.append(jogo[:])
    jogo.clear()
    cont += 1
for i, l in enumerate(megasena):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print(f'{"BOA SORTE!":=^39}')


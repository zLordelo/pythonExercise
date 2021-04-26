print('=' * 50)
print(f'\033[1;31m{"FUNÇÃO QUE CALCULA ÁREA":^50}\033[m')
print('=' * 50)
'''Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) 
e mostre a área do terreno.'''
def area(l, c):
    a = l * c
    print(f'Um terreno com \033[1m{l:.1f}m x {c:.1f}m\033[m tem área de \033[1m{a:.1f}m²\033[m')

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
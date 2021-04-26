from time import sleep
print('=' * 50)
print(f'\033[1;31m{"BOLETIM COM LISTAS COMPOSTAS":^50}\033[m')
print('=' * 50)
'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos 
e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de
cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
alunos = list()
aluno = list()
while True:
    opção = ' '
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    alunos.append(aluno[:])
    aluno.clear()
    while opção not in 'NnSs':
        opção = str(input('Deseja continuar [S/N]: ')).strip()[0]
    if opção in 'Nn':
        break

print('=' * 50)
print(f'\033[1;31m{"MAT.":<5}', f'{"NOME":<15}', f'{"MÉDIA":<5}\033[m')
for i, a in enumerate(alunos):
    print(f'\033[33m{i:<5}', f'{a[0].upper():<15}', f'{(a[1]+a[2])/2:<5.1f}\033[m')
print('=' * 50)

while True:
    opção = int(input('Digite a MATRÍCULA e veja a NOTA do aluno [-1 para \033[1;31mPARAR\033[m]: '))
    if opção < 0:
        break
    print(f'A nota de \033[1;33m{alunos[opção][0].upper()}\033[m foi: \033[1;33m{alunos[opção][1]}\033[m, \033[1;33m{alunos[opção][2]}\033[m')
print('=' * 50)
print('\033[1;31mFINALIZANDO\033[m', end='')
sleep(0.5)
print('\033[1;31m.\033[m', end='')
sleep(0.5)
print('\033[1;31m.\033[m', end='')
sleep(0.5)
print('\033[1;31m.\033[m')
sleep(0.5)
print('Obrigado pela atenção, volte sempre!')
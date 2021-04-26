import random

a1 = input('Digite o nome do aluno: ')
a2 = input('Digite o nome do aluno: ')
a3 = input('Digite o nome do aluno: ')
a4 = input('Digite o nome do aluno: ')

list = [a1, a2, a3, a4]

sorteio = random.choice(list)

print('O aluno sorteado foi {}.'.format(sorteio))
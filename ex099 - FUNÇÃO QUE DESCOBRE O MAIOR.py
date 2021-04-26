print('=' * 50)
print(f'\033[1;31m{"FUNÇÃO QUE DESCOBRE O MAIOR":^50}\033[m')
print('=' * 50)
'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros. Seu programa tem que analisar 
todos os valores e dizer qual deles é o maior.'''


def maior(* num):
    mai = cont = 0
    for n in num:
        if cont == 0:
            mai = n
        else:
            if n > mai:
                mai = n
        cont += 1
    print(f'Recebi os valores \033[1m{num}\033[m'
          f'\nO maior valor é \033[1m{mai}\033[m.')
    print('=' * 50)


maior(5, 15, 105, 6, 9, 203, 350, 351, 450, 451)
maior(5, 20, -50, -500, 500, 5062, 2, 8)
maior(-150, 150, 0)
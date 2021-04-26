print('=' * 50)
print(f'\033[1;31m{"FUNÇÃO PARA FATORIAL":^50}\033[m')
print('=' * 50)
'''Exercício Python 102: Crie um programa que tenha uma função fatorial() 
que receba dois parâmetros: o primeiro que indique o número a calcular 
outro chamado show, que será um valor lógico (opcional) indicando se 
será mostrado ou não na tela o processo de cálculo do fatorial.'''

def fatorial(n, show=True):
    f = 1
    if show:
        for c in range(n, 0, -1):
            print(c, end='')
            f *= c
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    else:
        for c in range(n, 0, -1):
            f *= c
    return f



num = int(input('Digite um número: '))
conta = str(input('Quer ver a conta [S/N]: '))
if conta in 'Ss':
    conta = True
elif conta in 'Nn ':
    conta = False

print('=' * 50)
print(fatorial(num, conta))

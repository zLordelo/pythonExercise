from random import randint
from time import sleep
print('=' * 50)
print(f'\033[1;31m{"FUNÇÃO PARA SORTEAR E SOMAR":^50}\033[m')
print('=' * 50)
'''Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas 
funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e 
vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos 
os valores pares sorteados pela função anterior.'''


# Função que sorteia 5 números
def sorteio(lst):
    for n in range(0, 5):
        lst.append(randint(0,10))
    print('Sorteando 5 valores: ', end='')
    sleep(1)
    print(f'{lst}')
    print()


# Função que soma os valores PAR sorteados anteriormente
def somapar(lst):
    soma = 0
    for n in lst:
        if n % 2 == 0:
            soma += n
    if soma == 0:
        print('Nenhum número PAR foi encontrado.')
    else:
        print(f'A soma dos números PAR é: {soma}')

# Atribuição da lista e chamada das funções
numeros = list()
sorteio(numeros)
somapar(numeros)

from time import sleep
print('=' * 50)
print(f'\033[1;31m{"FUNÇÃO DE CONTADOR":^50}\033[m')
print('=' * 50)
'''Exercício Python 098: Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar 
três contagens através da função criada: 
a) de 1 até 10, de 1 em 1 
b) de 10 até 0, de 2 em 2 
c) uma contagem personalizada'''


# Função
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}:')
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += passo
        print('→ Fim!')
    else:
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
        print('→ Fim!')
    sleep(1)
    print('=' * 50)


# Chamada A e B
contador(1, 10, 1)
contador(10, 0, -2)
# Programa principal
print(f'\033[1;31m{"PERSONALIZE SUA CONTAGEM":^50}\033[m')
print('=' * 50)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)


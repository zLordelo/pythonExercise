print('=' * 50)
print(f'\033[1;31m{"EXTRAINDO DADOS DE UMA LISTA":^50}\033[m')
print('=' * 50)
'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.               
Depois disso, mostre: A) Quantos números foram digitados. 
B) A lista de valores, ordenada de forma decrescente. 
C) Se o valor 5 foi digitado e está ou não na lista.'''

lista = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    opção = str(input('Deseja continuar [S/N]: ')).strip()[0]
    if opção in 'Nn':
        break
print('=' * 50)
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} valores.')
print(f'Sua lista em ordem decrescente: {lista}')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
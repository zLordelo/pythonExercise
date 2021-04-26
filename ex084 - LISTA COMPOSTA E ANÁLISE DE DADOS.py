print('=' * 50)
print(f'\033[1;31m{"LISTA COMPOSTA E ANÁLISE DE DADOS":^50}\033[m')
print('=' * 50)
'''Exercício Python 084: Faça um programa que leia nome e peso de várias 
pessoas, guardando tudo em uma lista. No final, mostre:                                                                                                    
A) Quantas pessoas foram cadastradas.                                                                                                                
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.'''

pessoas = list()
pessoa = list()
maior = menor = 0

while True:
    opção = ' '
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    while opção not in 'SsNn':
        opção = str(input('Deseja continuar [S/N]: ')).strip()[0]
    if opção in 'Nn':
        break
print('=' * 50)
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'\033[1m>{p[0]}<\033[m '.upper(), end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'\033[1m>{p[0]}<\033[m '.upper(), end='')

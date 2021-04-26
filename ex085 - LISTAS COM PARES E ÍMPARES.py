print('=' * 50)
print(f'\033[1;31m{"LISTAS COM PARES E ÍMPARES":^50}\033[m')
print('=' * 50)
'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e 
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
No final, mostre os valores pares e ímpares em ordem crescente.'''
valores = [[], []]

for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)
valores[0].sort()
valores[1].sort()
print(f'Os valores PAR digitados foram: {valores[0]}')
print(f'Os valores ÍMPAR digitados foram: {valores[1]}')
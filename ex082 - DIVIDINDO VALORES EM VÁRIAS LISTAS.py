print('=' * 50)
print(f'\033[1;31m{"DIVIDINDO VALORES EM VÁRIAS LISTAS":^50}\033[m')
print('=' * 50)
'''Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores 
ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas.'''
lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    opção = str(input('Deseja continuar [S/N]: ')).strip()[0]
    if opção in 'Nn':
        break
print(f'Sua lista possui os valores: {lista}')
listapar = []
listaimpar = []
for valor in lista:
    if valor % 2 == 0:
        listapar.append(valor)
    else:
        listaimpar.append(valor)
print(f'Sua lista com valores PAR: {listapar}')
print(f'Sua lista com Valores ÍMPAR: {listaimpar}')
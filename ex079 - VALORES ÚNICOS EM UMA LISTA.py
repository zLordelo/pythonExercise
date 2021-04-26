print('=' * 50)
print(f'\033[1;31m{"VALORES ÚNICOS EM UMA LISTA":^50}\033[m')
print('=' * 50)
'''Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos 
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

valores = []
while True:
    valor = int(input('Digite um número: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não adicionarei a lista.')
    opção = str(input('Deseja continuar [S/N]: ')).split()[0]
    if opção in 'Nn':
        break
valores.sort()
print(f'\nVocê digitou os valores: {valores}')

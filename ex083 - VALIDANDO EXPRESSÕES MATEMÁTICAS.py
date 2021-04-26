print('=' * 50)
print(f'\033[1;31m{"VALIDANDO EXPRESSÕES MATEMÁTICAS":^50}\033[m')
print('=' * 50)
'''Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que 
use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os 
parênteses abertos e fechados na ordem correta.'''
expr = str(input('Digite uma expressão: '))
lista = []
for simb in expr:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está inválida!')

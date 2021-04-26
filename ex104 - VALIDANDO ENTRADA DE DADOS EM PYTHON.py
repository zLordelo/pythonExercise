print('=' * 50)
print(f'\033[1;31m{"VALIDANDO ENTRADA DE DADOS EM PYTHON":^50}\033[m')
print('=' * 50)
'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), 
que vai funcionar de forma semelhante ‘a função input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico. 
Ex: n = leiaInt(‘Digite um n: ‘)'''


def leiaInt(msg):
    n = input(msg)
    while n.isnumeric() == False:
        print('\033[1;31m[ERRO]\033[m Digite somente números.')
        n = input(msg)
    if n.isnumeric():
        return n


num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}.')
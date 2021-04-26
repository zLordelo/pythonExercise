print('=' * 50)
print(f'\033[1;31m{"FUNÇÃO PARA VOTAÇÃO":^50}\033[m')
print('=' * 50)
'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() 
que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando 
um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

#UTILIZANDO O CONCEITO DE ESCOPO DE IMPORTAÇÃO
#AQUI SÓ IRÁ SER IMPORTADO O MODULO DATETIME NA EXEC DA FUNÇÃO
def voto(ano):
    from datetime import datetime
    idade = datetime.today().year - ano
    if idade < 16:
        return f'IDADE: {idade} anos \nSeu voto está NEGADO na eleição atual.'
    elif idade >= 18 and idade <= 70:
        return f'IDADE: {idade} anos \nSeu voto é OBRIGATÓRIO na eleição atual.'
    else:
        return f'IDADE: {idade} anos \nSeu voto é OPCIONAL na eleição atual.'


nasc = int(input('Em que ano você nasceu: '))
print(voto(nasc))
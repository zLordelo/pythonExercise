print('=' * 50)
print(f'\033[1;31m{"ANALISANDO E GERANDO DICIONÁRIOS":^50}\033[m')
print('=' * 50)
'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias
notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)'''


def notas(*num, sit=False):
    notas = dict()
    notas['total'] = len(num)
    notas['maior'] = max(num)
    notas['menor'] = min(num)
    notas['media'] = sum(num)/len(num)
    if sit:
        if notas['media'] >= 7:
            notas['situação'] = 'ÓTIMO'
        elif notas['media'] >= 5:
            notas['situação'] = 'REGULAR'
        else:
            notas['situação'] = 'RUIM'
    return notas


boletim = notas(5, 2, 6, 11, 3, sit=True)
print(boletim)
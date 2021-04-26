print('=' * 50)
print(f'\033[1;31m{"DICIONÁRIOS EM PYTHON":^50}\033[m')
print('=' * 50)
'''Exercício Python 090: Faça um programa que leia nome e média de um 
aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.'''
boletim = {} #OU dict()
boletim['nome'] = str(input('Nome do aluno: ')).upper()
boletim['media'] = float(input('Média do aluno: '))
if boletim['media'] < 5:
    boletim['situacao'] = '\033[1;31mREPROVADO\033[m'
elif boletim['media'] < 7:
    boletim['situacao'] = '\033[1;33mRECUPERAÇÃO\033[m'
else:
    boletim['situacao'] = '\033[1;34mAPROVADO\033[m'
print('=' * 50)
print(f'\033[1;31m{"BOLETIM":^50}\033[m')
print('=' * 50)
print(f'Aluno: {boletim["nome"]}')
print(f'Média: {boletim["media"]}')
print(f'Situação: {boletim["situacao"]}')


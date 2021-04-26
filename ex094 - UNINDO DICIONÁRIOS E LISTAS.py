print('=' * 50)
print(f'\033[1;31m{"UNINDO DICIONÁRIOS E LISTAS":^50}\033[m')
print('=' * 50)
'''Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando 
os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média'''
cont = 1
pessoas = dict() #{}
grupo = list() #[]
mulheres = list() #[]
acima_media = list() #[]
idades = 0

while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO. Digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    idades += pessoas['idade']
    if pessoas['sexo'] in 'Ff':
        mulheres.append(pessoas.copy())
    grupo.append(pessoas.copy())
    media = idades / len(grupo)
    while True:
        resp = str(input('Deseja continuar [S/N]: ')).strip()[0]
        if resp in 'SsNn':
            break
        print('ERRO. Digite apenas S ou N.')
    if resp in 'Nn':
        break

print('=' * 50)
print(f'\033[1;31m{"RELATÓRIO ↓":^50}\033[m')
print('=' * 50)
print(f'\033[1mPessoas cadastradas:\033[m {len(grupo)}')
print(f'\033[1mMédia da idade:\033[m {media:.2f} anos')
print('=' * 50)
print(f'\033[1;33m{"LISTA DE MULHERES ↓":^50}\033[m')
for v in mulheres:
    print(f'\033[1m{v["nome"].upper():^50}\033[m')
print('=' * 50)
print(f'\033[1;33m{"PESSOAS ACIMA DA MÉDIA DE IDADE ↓":^50}\033[m')
for v in grupo:
    if v['idade'] > media:
        acima_media.append(v.copy())
for v in acima_media:
    print(f'\033[1m{v["nome"].upper()}\033[m com \033[1m{v["idade"]}\033[m anos')
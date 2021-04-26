from datetime import datetime
print('=' * 50)
print(f'\033[1;31m{"CADASTRO DE TRABALHADOR EM PYTHON":^50}\033[m')
print('=' * 50)
'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e 
carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e
o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
funcionario = dict()
funcionario['nome'] = str(input('Nome do funcionário: '))
funcionario['nasc'] = int(input('Ano de nascimento: '))
funcionario['idade'] = datetime.today().year - funcionario['nasc']
funcionario['ctps'] = int(input('CTPS (0 não tem): '))
if funcionario['ctps'] > 0 :
    funcionario['contrat'] = int(input('Ano de contratação: '))
    funcionario['apos'] = funcionario['idade'] + ((funcionario['contrat'] + 35) - datetime.today().year)
    funcionario['salario'] = float(input('Salário: R$ '))

print('=' * 50)
print(f'\033[1;31m{"DADOS DO TRABALHADOR":^50}\033[m')
print('=' * 50)

print(f'Nome: {funcionario["nome"]}')
print(f'Nascimento: {funcionario["nasc"]}')
print(f'Idade: {funcionario["idade"]} anos')
print(f'CTPS: {funcionario["ctps"]}')
if funcionario['ctps'] > 0:
    print(f'Data de contratação: {funcionario["contrat"]}')
    print(f'Salário: R$ {funcionario["salario"]:.2f}')
    print(f'Aposenta-se com: {funcionario["apos"]} anos')
print('=' * 50)
print('=' * 50)
print('\033[1;31mANÁLISE DE DADOS DO GRUPO\033[m'.center(60))
print('=' * 50)

maiores = homens = mulheres_menores = 0

while True:
    print('\033[1;31mCADASTRE UMA PESSOA\033[m')
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menores += 1
    if idade > 18:
        maiores += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja continua [S/N]: ')).strip().upper()[0]
    print('=' * 50)
    if opcao == 'N':
        break
print('\033[34mANALISANDO OS DADOS...\033[m')
print(f'''Foram cadastrados {maiores} pessoa(s) maiores de 18 anos.
Existe {homens} homen(s) no cadastro.
Existe {mulheres_menores} mulhere(s) menor(es) de idade.''')
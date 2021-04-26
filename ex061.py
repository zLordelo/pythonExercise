print('=' * 50)
print('\033[1;31mPROGRESSÃO ARITMÉTICA V2.0 - WHILE\033[m'.center(60))
print('''\033[1;31m10 TERMOS\033[m'''.center(60))
print('=' * 50)

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('\033[1m{}\033[m → '. format(termo), end='')
    termo += razao
    cont += 1
print('\033[1;33mFIM\033[m')
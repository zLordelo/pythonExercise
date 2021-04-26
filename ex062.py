print('=' * 50)
print('\033[1;31mPROGRESSÃO ARITMÉTICA V2.0 - WHILE\033[m'.center(60))
print('=' * 50)

primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('\033[1m{}\033[m → '. format(termo), end='')
        termo += razao
        cont += 1
    print('\033[1;33mPAUSA\033[m')
    mais = int(input('Quantos termos gostaria de ver a mais? '))
print('\033[1;33mProgressão finalizada com {} termos visualizados.\033[m'.format(total))
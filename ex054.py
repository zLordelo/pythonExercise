import datetime
print('=' * 50)
print('\033[1;31mGRUPO DA MAIORIDADE\033[m'.center(60))
print('=' * 50)
ano = datetime.datetime.now().year
maiores = 0
menores = 0
for c in range(1, 8):
    nasc = int(input('Em que ano a  {}º nasceu? '.format(c)))
    idade = ano - nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print('Das idades avaliadas \033[1;31m{}\033[m estão na MAIORIDADE e \033[1;31m{}\033[m estão na MENORIDADE.'.format(maiores, menores))
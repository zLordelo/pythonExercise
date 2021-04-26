print('=' * 50)
print('\033[1;31mVERIFICADOR DE NÚMEROS PRIMOS\033[m'.center(60))
print('=' * 50)

num = int(input('Digite um número: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m{}\033[m'.format(c), end=' ')
        cont += 1
    else:
        print('{}'.format(c), end=' ')
print('\nO número \033[1;31m{}\033[m é divisível por \033[1;31m{} números\033[m.'.format(num, cont))
if cont == 2:
    print('Portanto ele \033[1;31mÉ UM NÚMERO PRIMO\033[m.')
else:
    print('Portanto, ele \033[1;31mNÃO É UM NÚMERO PRIMO\033[m.')
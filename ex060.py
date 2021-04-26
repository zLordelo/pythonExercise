from time import sleep
print('=' * 50)
print('\033[1;31mCÁLCULO DO FATORIAL - WHILE\033[m'.center(60))
print('=' * 50)

num = int(input('Digite um número: '))
cont = num
fat = 1

print('\033[1;31mCALCULANDO...\033[m')
sleep(0.5)
print('\033[1;31m{}!\033[m = '.format(num), end='')

while cont > 0:
    print('{} '.format(cont), end='')
    print('x ' if cont > 1 else '= ', end='')
    fat *= cont #ou fat = fat * cont
    cont -= 1
print('\033[1;31m{}\033[m'.format(fat))
print('O \033[1;31mFATORIAL\033[m de \033[1;31m{}\033[m é igual a \033[1;31m{}\033[m'.format(num, fat))

# OU PODE SER FEITO USANDO MÓDULO MATH (FACTORIAL) ↓↓↓
'''from math import factorial
num = int(input('Digite um número: '))
fat = factorial(num)
print('O \033[1;31mFATORIAL\033[m de \033[1;31m{}\033[m é igual a \033[1;31m{}\033[m'.format(num, fat))'''
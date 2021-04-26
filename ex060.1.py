from time import sleep
print('=' * 50)
print('\033[1;31mCÁLCULO DO FATORIAL - FOR\033[m'.center(60))
print('=' * 50)

num = int(input('Digite um número: '))
fat = 1
print('CALCULANDO...')
sleep(0.5)
print('{}! = '.format(num), end='')
for c in range(num, 0, -1):
    print('{} '.format(c), end='')
    print('x ' if c > 1 else '= ', end='')
    fat *= c
print(fat)
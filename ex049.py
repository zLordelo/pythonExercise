print('=' * 50)
print('\033[1;31mTABUADA v2.0\033[m'.center(50))
print('=' * 50)
n = int(input('Digite um número: '))
print('=' * 20)
for c in range(1,11):
    x = n * c
    print('{} x {:2} = {}'.format(n, c, x))
print('=' * 20)
print('=' * 50)
print('\033[1;31mSEQUÊNCIA DE FIBONACCI\033[m'.center(60))
print('=' * 50)

termos = int(input('Quantos termos deseja vizualizar? '))
cont = 3
t1 = 0
t2 = 1
print('{} → {} → '.format(t1, t2), end='')
while cont <= termos:
    t3 = t1 + t2
    print('{} → '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont +=1
print('FIM')
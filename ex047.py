from time import sleep
print('=' * 50)
print('\033[1;31mNÚMEROS PARES DE 1 Á 50\033[m'.center(50))
print('=' * 50)
sleep(1)
print('\033[1;31mPENSANDO...\033[m')
sleep(1)
for c in range(1, 51):
    if c % 2 == 0:
        print(c)
        sleep(0.3)
sleep(1)
print('ACABOU!')
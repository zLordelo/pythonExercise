from time import sleep

print('=' * 25)
print('\033[1mCONTAGEM REGRESSIVA\033[m'.center(32))
print('=' * 25)

for c in range(10, -1, -1):
    print (c)
    sleep(1)
print('=' * 20)
print('\033[1;33mFELIZ ANO NOVO!\033[m'.center(30))
print('=' * 20)
from time import sleep
print('=' * 50)
print('\033[1;31mTABUADA V3.0\033[m'.center(60))
print('=' * 50)

while True:
    num = int(input('Digite o número qual deseja ver a tabuada: '))
    if num < 0:
        break
    for c in range (1, 11):
        print(f'{num} x {c} = {num * c}')
    print('=' * 50)
sleep(0.5)
print('\nFINALIZANDO...')
sleep(1)
print('\033[1;31mTABUADA V3.0 FINALIZADA COM SUCESSO.\033[m')
print('\033[1;33mObrigado pelo uso e volte sempre \033[1;31m\U0001F5A4\033[m')
from random import randint
print('=' * 50)
print('\033[1;31mPAR OU ÍMPAR\033[m'.center(60))
print('=' * 50)

ia = randint(0, 10)
vitorias = 0

while True:
    num = int(input('Escolha um número: '))
    opcao = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    soma = ia + num
    while opcao not in 'PI':
        opcao = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0]
    print(f'O computador jogou {ia} e você jogou {num}. O total é {soma}.')
    print('DEU PAR' if soma % 2 == 0 else 'DEU ÍMPAR')
    if soma % 2 == 0 and opcao in ('Pp'):
        print('\033[34mVOCÊ VENCEU!\033[m')
        vitorias += 1
    elif soma % 2 != 0 and opcao in ('Ii'):
        print('\033[34mVOCÊ VENCEU!\033[m')
        vitorias += 1
    else:
        break
print(f'\033[1;31mGAME OVER!\033[m Você venceu \033[31m{vitorias} vezes\033[m.')